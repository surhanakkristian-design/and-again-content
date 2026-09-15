#!/usr/bin/env python3
"""Brief 19 in-session pipeline (model = Claude subagents, no API key anywhere).

  pipeline.py next   --job 1 --batches 8 [--size 50]   -> writes runs/job_<id>/batch_<seq>.json (+ rows_<seq>.json)
  pipeline.py submit --job 1 --seq 12 [--seq 13 ...]   -> validates out_<seq>.json locally, POSTs accepted rows to the
                                                          chunk-sentences write path (which re-validates + guards), logs
  pipeline.py status --job 1

`next` uses the same SQL as the server (sentence_chunk_next_rows: unchunked, in scope, < max_attempts rejects in this
job) and skips rows already handed out to a pending batch (runs/job_<id>/pending.json) so parallel batches never overlap.
"""
import json, os, subprocess, sys, urllib.request, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.environ.get("AND_AGAIN_APP", os.path.expanduser("~/Projects/and-again"))  # the app checkout that holds the Supabase link (db query --linked)
URL = "https://abyrutykpvmzkfbesire.supabase.co/functions/v1/chunk-sentences"
KEY = "sb_publishable_OaVs6yUd1S4_53THo4cH4w_iYNdhmdD"  # public app key (supabase.ts)

def dbq(sql):
    out = subprocess.run(["npx", "-y", "supabase@2.116.0", "db", "query", sql, "--linked", "-o", "json"],
                         cwd=APP, capture_output=True, text=True).stdout
    i = out.find('{\n  "boundary"');  i = out.find('{') if i < 0 else i
    d, _ = json.JSONDecoder().raw_decode(out[i:])  # tolerate the CLI's trailing update notice
    return d["rows"]

def arg(name, default=None):
    return sys.argv[sys.argv.index(name)+1] if name in sys.argv else default

def run_dir(job):
    d = os.path.join(HERE, "runs", f"job_{job}"); os.makedirs(d, exist_ok=True); return d

def load(p, default):
    return json.load(open(p)) if os.path.exists(p) else default

import re as _re
# Part 12: constructions the whole-phrase matcher cannot vouch for yet; rows that fail ONLY the cap/floor because of
# them are parked in gap.json (not posted) until the matcher decision is taken. Per language.
GAP_RE = {
    "fr": _re.compile(r"\b(?:beaucoup|peu|trop|assez|tant|autant|combien|plus|moins|tellement|énormément)\s+d(?:e\b|')"
                      r"|\bà travers\b|\bjusqu'(?:au|aux|à|en)\b|\by a-t-il\b|\bil y a\b|\bauprès d"
                      r"|\bde (?:tout |très |si |trop )?(?:petit|grand|gros|long|bon|beau|vieux|jeune|nouveau|autre|joli|belle|bonne|grande|petite|longue|vieille|grosse|nouvelle|jolie)s?\b"
                      r"|\b(?:onze|douze|treize|quatorze|quinze|seize|dix-sept|dix-huit|dix-neuf|trente|quarante|cinquante|soixante|quatre-vingts?|quatre-vingt-dix)\b", _re.I),
}

def log(job, obj):
    line = f"{datetime.datetime.now().isoformat(timespec='seconds')} {json.dumps(obj, ensure_ascii=False)}"
    print(line, flush=True); open(os.path.join(run_dir(job), "run.log"), "a").write(line + "\n")

def cmd_next():
    job = int(arg("--job")); nb = int(arg("--batches", 8)); size = int(arg("--size", 50))
    d = run_dir(job); pending = load(os.path.join(d, "pending.json"), {})
    taken = {i for ids in pending.values() for i in ids} | {h["id"] for h in load(os.path.join(d, "hold.json"), [])} \
          | {x["id"] for x in load(os.path.join(d, "deferred.json"), [])} \
          | {x["id"] for x in load(os.path.join(d, "gap.json"), [])}  # parked (next deploy / Part 12 decision): not handed out again
    rows = dbq(f"select * from sentence_chunk_next_rows({job}, {nb*size + len(taken)}) order by id")
    rows = [r for r in rows if r["id"] not in taken][:nb*size]
    seq = load(os.path.join(d, "seq.json"), 0); made = []
    for b in range(0, len(rows), size):
        part = rows[b:b+size]; seq += 1
        json.dump(part, open(os.path.join(d, f"rows_{seq}.json"), "w"), ensure_ascii=False)
        json.dump([{"id": r["id"], "sentence": r["full_sentence"], "answer": r["correct_answer"]} for r in part],
                  open(os.path.join(d, f"batch_{seq}.json"), "w"), ensure_ascii=False, indent=0)
        pending[str(seq)] = [r["id"] for r in part]; made.append(seq)
    json.dump(seq, open(os.path.join(d, "seq.json"), "w")); json.dump(pending, open(os.path.join(d, "pending.json"), "w"))
    log(job, {"next": made, "rows": len(rows)})
    print(json.dumps({"batches": made, "dir": d}))

def cmd_submit():
    job = int(arg("--job")); seqs = [int(sys.argv[i+1]) for i, a in enumerate(sys.argv) if a == "--seq"]
    d = run_dir(job); pending = load(os.path.join(d, "pending.json"), {})
    jrow = dbq(f"select run_token, language_code from sentence_chunk_jobs where id = {job}")[0]; token = jrow["run_token"]; LANG = jrow["language_code"]
    sys.path.insert(0, HERE); import validate_chunks as V
    server_min = int(arg("--server-min-pieces", 3))  # the DEPLOYED function's floor (v5: three pieces by length); shorter valid splits are deferred
    defer_ex = "--defer-exemptions" in sys.argv  # local validator ahead of the deployed one: park exempted rows for submit-deferred
    for seq in seqs:
        rows = json.load(open(os.path.join(d, f"rows_{seq}.json"))); outp = os.path.join(d, f"out_{seq}.json")
        if not os.path.exists(outp): log(job, {"seq": seq, "error": "no output file"}); continue
        outs = {o["id"]: o for o in json.load(open(outp))}
        hold_thr = float(arg("--hold", 0)) or 0.0
        firstp = os.path.join(d, f"first_{seq}.json"); first = {x["id"]: x for x in json.load(open(firstp))} if os.path.exists(firstp) else {}
        held = load(os.path.join(d, "hold.json"), [])
        ok, bad, deferred, gap = [], [], [], []
        exempt = {}  # Brief 20 Part 8: exemption name -> count for this batch (local validator); the server reports its own
        for r in rows:
            o = outs.get(r["id"]); reasons, ex = V.check2(r, o, LANG) if o else (["missing_output"], [])
            for e in ex: exempt[e] = exempt.get(e, 0) + 1
            if r["id"] in first:
                # pass-2 batch: keep the second pass only if valid and its largest share is not worse;
                # fall back to the first pass only if THAT still passes the (current) validator.
                f = first[r["id"]]; f_ok = not V.check(r, f, LANG)
                if not reasons and (not f_ok or V.largest_share(r["full_sentence"], o["chunks"]) <= V.largest_share(r["full_sentence"], f["chunks"])):
                    chosen = o
                elif f_ok:
                    chosen = f; reasons = []
                    log(job, {"seq": seq, "pass2_kept_first": r["id"], "pass2_reasons": V.check(r, o, LANG) if o else ["missing_output"]})
                else:
                    bad.append({"id": r["id"], "chunks": (o or {}).get("chunks"), "alternatives": (o or {}).get("alternatives", []), "reasons": reasons or ["first_pass_invalid"]}); continue
                if len(chosen["chunks"]) < server_min:
                    deferred.append({"id": r["id"], "chunks": chosen["chunks"], "alternatives": chosen.get("alternatives", [])}); continue
                ok.append({"id": r["id"], "chunks": chosen["chunks"], "alternatives": chosen.get("alternatives", []), "reasons": []}); continue
            if not reasons and hold_thr and len(r["full_sentence"].split()) >= int(arg("--hold-minwords", 12)) and V.largest_share(r["full_sentence"], o["chunks"]) > hold_thr:
                if r["id"] not in {h["id"] for h in held}: held.append({**r, "chunks": o["chunks"], "alternatives": o.get("alternatives", [])})
                continue
            # DEFER_EX parks only what the DEPLOYED function (v6) cannot take yet: the floor exemption above 9 words (v7)
            if not reasons and (len(o["chunks"]) < server_min or (defer_ex and ex and (
                    ("floor_min_pieces" in ex and V.word_count(r["full_sentence"]) > 9)
                    # Part 12: v6 still counts a French " ?" / " !" token as a word inside a piece, so an exemption that
                    # rests on a piece like "fait-il ?" being one word waits for v7 as well
                    or any(len(c.split()) > 1 and any(not _re.search(r"[^\W_]", t) for t in c.split()) for c in o["chunks"])))):
                deferred.append({"id": r["id"], "chunks": o["chunks"], "alternatives": o.get("alternatives", [])}); continue
            if reasons and o and GAP_RE.get(LANG) and all(k.startswith("dominant_piece") or k == "piece_count_3" for k in reasons) \
               and (GAP_RE[LANG].search(r["full_sentence"]) or (LANG == "fr" and any(
                    _re.match(r"(?i)[ldnsjmtc]'\S", c.strip()) and len(c.split()) > 1 for c in o["chunks"]))):
                # (fr) a piece opening on an elided article/pronoun ("L'œuf frit") is one token to the matcher, never a phrase
                # Part 12: the whole-phrase matcher does not know this construction yet (fr quantifier + de, à travers,
                # jusqu'au, y a-t-il); park the row locally instead of spending a server attempt on it
                gap.append({"id": r["id"], "chunks": o["chunks"], "alternatives": o.get("alternatives", []), "reasons": reasons}); continue
            (ok if not reasons else bad).append({"id": r["id"], "chunks": (o or {}).get("chunks"), "alternatives": (o or {}).get("alternatives", []), "reasons": reasons})
        json.dump(held, open(os.path.join(d, "hold.json"), "w"), ensure_ascii=False)
        if gap:
            gp = os.path.join(d, "gap.json"); gl = load(gp, []); known = {x["id"] for x in gl}
            gl += [x for x in gap if x["id"] not in known]; json.dump(gl, open(gp, "w"), ensure_ascii=False)
        if deferred:  # valid locally, below the deployed floor: parked until the function is redeployed (submit-deferred)
            dp = os.path.join(d, "deferred.json"); dl = load(dp, []); known = {x["id"] for x in dl}
            dl += [x for x in deferred if x["id"] not in known]; json.dump(dl, open(dp, "w"), ensure_ascii=False)
        # post EVERYTHING (accepted and rejected): the server re-validates, and rejects must be logged server-side
        # so the retry bookkeeping (attempts) lives in one place.
        # Locally rejected rows are posted with EMPTY chunks so the server logs the attempt (retry bookkeeping)
        # but can never write them, even when the deployed validator is older than the local one.
        payload = {"jobId": job, "runToken": token, "rows": [{"id": x["id"], "chunks": x["chunks"] or [], "alternatives": x["alternatives"] or []} for x in ok]
                   + [{"id": x["id"], "chunks": [], "alternatives": []} for x in bad]}
        for x in bad: log(job, {"seq": seq, "local_reject": x["id"], "reasons": x["reasons"], "chunks": x["chunks"]})
        req = urllib.request.Request(URL, data=json.dumps(payload).encode(), method="POST",
              headers={"Content-Type": "application/json", "apikey": KEY, "Authorization": f"Bearer {KEY}"})
        resp = {"error": "not sent"}
        for attempt in range(3):  # transient network errors (SSL bad record mac, resets) get two retries
            try:
                with urllib.request.urlopen(req, timeout=120) as r: resp = json.loads(r.read()); break
            except urllib.error.HTTPError as e:
                resp = {"error": f"HTTP {e.code}: {e.read()[:300]!r}"}; break
            except Exception as e:
                resp = {"error": f"request failed: {e!r}"}; import time; time.sleep(3 * (attempt + 1))
        if "error" in resp and "request failed" in resp["error"]:
            # urllib's TLS path fails persistently on some payloads (SSL bad record mac); curl is a separate stack.
            tmp = os.path.join(d, f"payload_{seq}.json"); open(tmp, "w").write(json.dumps(payload))
            cp = subprocess.run(["curl", "-sS", "--max-time", "120", "-X", "POST", URL, "-H", "Content-Type: application/json",
                                 "-H", f"apikey: {KEY}", "-H", f"Authorization: Bearer {KEY}", "--data-binary", f"@{tmp}"],
                                capture_output=True, text=True)
            try: resp = json.loads(cp.stdout); resp["via"] = "curl"
            except Exception: resp = {"error": f"curl failed: {cp.stderr[:200]} {cp.stdout[:200]}"}
            os.remove(tmp)
        if "error" not in resp:
            pending.pop(str(seq), None); json.dump(pending, open(os.path.join(d, "pending.json"), "w"))
        log(job, {"seq": seq, "local_accepted": len(ok), "local_rejected": len(bad), "held_over40": len(held), "deferred_short": len(deferred), "gap_parked": len(gap), "local_reasons": sorted({r for x in bad for r in x["reasons"]}), "exemptions": exempt, "server": resp})

def cmd_submit_deferred():
    """Post runs/job_<id>/deferred.json (valid 3-piece splits) once the edge function accepts them."""
    job = int(arg("--job")); d = run_dir(job); dp = os.path.join(d, arg("--file", "deferred.json")); rows = load(dp, [])
    token = dbq(f"select run_token from sentence_chunk_jobs where id = {job}")[0]["run_token"]
    # Part 14: --file gap.json posts the parked matcher-gap rows; rows that already carry chunks on the table are skipped
    if rows and arg("--file") and "--overwrite" not in sys.argv:
        ids = ",".join(str(x["id"]) for x in rows)
        done = {r["id"] for r in dbq(f"select id from exercise_localizations where id in ({ids}) and chunks is not null and jsonb_array_length(chunks) > 0")}
        skipped = [x for x in rows if x["id"] in done]; rows = [x for x in rows if x["id"] not in done]
        print(json.dumps({"file": arg("--file"), "to_post": len(rows), "skipped_already_chunked": len(skipped)}))
    for b in range(0, len(rows), 200):
        part = rows[b:b+200]
        payload = {"jobId": job, "runToken": token, "rows": [{"id": x["id"], "chunks": x["chunks"], "alternatives": x.get("alternatives", [])} for x in part]}
        req = urllib.request.Request(URL, data=json.dumps(payload).encode(), method="POST", headers={"Content-Type": "application/json", "apikey": KEY, "Authorization": f"Bearer {KEY}"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r: resp = json.loads(r.read())
        except Exception as e: resp = {"error": repr(e)}
        log(job, {"submit_deferred": len(part), "server": resp}); print(json.dumps(resp)[:400])
    if rows and "error" not in resp: json.dump([], open(dp, "w"))

def exemption_totals(job):
    """Brief 20 Part 8: exemptions the server accepted in this run (summed from run.log), by name."""
    tot = {}; lp = os.path.join(run_dir(job), "run.log")
    if not os.path.exists(lp): return tot
    for line in open(lp):
        try: j = json.loads(line[line.index("{"):])
        except Exception: continue
        srv = j.get("server") or {}
        for k, v in (srv.get("exemptions") or {}).items(): tot[k] = tot.get(k, 0) + v
    return tot

def cmd_batch_ids():
    """Part 15: build batches from an explicit id list (--ids <json list>) for re-runs; rows come from the table."""
    job = int(arg("--job")); d = run_dir(job); ids = json.load(open(arg("--ids"))); size = int(arg("--size", 50))
    lang = dbq(f"select language_code from sentence_chunk_jobs where id = {job}")[0]["language_code"]
    rows = dbq("select el.id, e.exercise_type_id, el.full_sentence, el.correct_answer from exercise_localizations el join exercises e on e.id = el.exercise_id "
               f"where el.language_code = '{lang}' and el.id in ({','.join(str(i) for i in ids)}) order by el.id")
    pending = load(os.path.join(d, "pending.json"), {}); seq = load(os.path.join(d, "seq.json"), 0); made = []
    for b in range(0, len(rows), size):
        part = rows[b:b+size]; seq += 1
        json.dump(part, open(os.path.join(d, f"rows_{seq}.json"), "w"), ensure_ascii=False)
        json.dump([{"id": r["id"], "sentence": r["full_sentence"], "answer": r["correct_answer"]} for r in part], open(os.path.join(d, f"batch_{seq}.json"), "w"), ensure_ascii=False, indent=0)
        pending[str(seq)] = [r["id"] for r in part]; made.append(seq)
    json.dump(seq, open(os.path.join(d, "seq.json"), "w")); json.dump(pending, open(os.path.join(d, "pending.json"), "w"))
    log(job, {"batch_ids": made, "rows": len(rows), "missing": len(ids) - len(rows)}); print(json.dumps({"batches": made, "rows": len(rows), "missing": len(ids) - len(rows)}))

def cmd_status():
    job = int(arg("--job"))
    row = dbq(f"select id, language_code, status, calls, rows_seen, rows_accepted, rows_rejected from sentence_chunk_jobs where id={job}")[0]
    row["exemptions_accepted"] = exemption_totals(job)  # Part 8: reported at the end of every run, per language
    print(json.dumps(row))
    print(json.dumps(dbq("select * from sentence_chunk_progress order by 1")))

def _make_pass2_batches(job, held, size=50):
    d = run_dir(job); pending = load(os.path.join(d, "pending.json"), {}); seq = load(os.path.join(d, "seq.json"), 0); made = []
    seen = set(); held = [h for h in held if not (h["id"] in seen or seen.add(h["id"]))]
    for b in range(0, len(held), size):
        part = held[b:b+size]; seq += 1
        json.dump([{k: r[k] for k in ("id", "exercise_type_id", "full_sentence", "correct_answer")} for r in part], open(os.path.join(d, f"rows_{seq}.json"), "w"), ensure_ascii=False)
        json.dump([{"id": r["id"], "chunks": r["chunks"], "alternatives": r.get("alternatives", [])} for r in part], open(os.path.join(d, f"first_{seq}.json"), "w"), ensure_ascii=False)
        json.dump([{"id": r["id"], "sentence": r["full_sentence"], "answer": r["correct_answer"], "first_pass": r["chunks"]} for r in part],
                  open(os.path.join(d, f"batch_{seq}.json"), "w"), ensure_ascii=False, indent=0)
        pending[str(seq)] = [r["id"] for r in part]; made.append(seq)
    json.dump(seq, open(os.path.join(d, "seq.json"), "w")); json.dump(pending, open(os.path.join(d, "pending.json"), "w"))
    return made

def cmd_pass2():
    job = int(arg("--job")); d = run_dir(job); held = load(os.path.join(d, "hold.json"), [])
    made = _make_pass2_batches(job, held); json.dump([], open(os.path.join(d, "hold.json"), "w"))
    log(job, {"pass2_batches": made, "rows": len(held)}); print(json.dumps({"batches": made, "rows": len(held)}))

def cmd_pass2db():
    job = int(arg("--job")); lang = arg("--lang"); thr = float(arg("--hold", 0.40))
    rows = dbq(f"select el.id, e.exercise_type_id, el.full_sentence, el.correct_answer, el.chunks, el.correct_alternative as alternatives from exercise_localizations el join exercises e on e.id=el.exercise_id where el.language_code='{lang}' and el.chunks is not null and e.exercise_type_id<>69")
    held = [r for r in rows if max(len(p.split()) for p in r["chunks"]) / len(r["full_sentence"].split()) > thr]
    for r in held: r["alternatives"] = r["alternatives"] or []
    made = _make_pass2_batches(job, held); log(job, {"pass2db_batches": made, "rows": len(held)}); print(json.dumps({"batches": made, "rows": len(held)}))

def cmd_census():
    """Brief 20 Part 8: exemptions on the LIVE table for one language, by name (cap_whole_phrase / floor_min_pieces),
    plus rows that fail the current validator. Run at the end of every language run and put both numbers in the report."""
    lang = arg("--lang"); sys.path.insert(0, HERE); import validate_chunks as V
    rows = dbq(f"select el.id, el.full_sentence, el.correct_answer, el.chunks from exercise_localizations el join exercises e on e.id=el.exercise_id where el.language_code='{lang}' and el.chunks is not null and e.exercise_type_id<>69")
    ex, bad, ex_ids = {}, {}, {}
    for r in rows:
        reasons, e = V.check2(r, {"chunks": r["chunks"], "alternatives": []}, lang)
        for k in e: ex[k] = ex.get(k, 0) + 1; ex_ids.setdefault(k, []).append(r["id"])
        for k in reasons: k = "dominant_piece" if k.startswith("dominant") else k; bad[k] = bad.get(k, 0) + 1
    print(json.dumps({"language": lang, "rows": len(rows), "exemptions_by_name": ex, "exemption_share": {k: round(v / max(1, len(rows)), 4) for k, v in ex.items()}, "rule_failures": bad}))
    json.dump(ex_ids, open(os.path.join(HERE, "runs", f"census_{lang}_exemptions.json"), "w"))

{"next": cmd_next, "submit": cmd_submit, "submit-deferred": cmd_submit_deferred, "status": cmd_status, "pass2": cmd_pass2, "pass2db": cmd_pass2db, "census": cmd_census, "batch-ids": cmd_batch_ids}[sys.argv[1]]()

# ---------------------------------------------------------------------------
# Brief 20 Part 1: second pass for rows whose largest piece holds > 40% of the words.
#   submit ... --hold 0.40        -> such rows are NOT posted; they go to runs/job_<id>/hold.json (with first pass)
#   pipeline.py pass2 --job N     -> turns hold.json into one or more batches (batch_<seq>.json + first_<seq>.json)
#   submit --seq <pass2 seq>      -> posts the second pass when it is valid and not worse; otherwise the first pass
# Brief 20 Part 8: every batch line carries "exemptions" (local) and server.exemptions (accepted); `status --job N` sums the
#   accepted ones per job = per language, by name; `census --lang xx` counts them on the live table, by name. Both numbers
#   (cap_whole_phrase and floor_min_pieces separately) go into the report at the end of EVERY language run. A large
#   number is a signal that the ladder is wrong for that language and the exemption is carrying it.
#   pipeline.py pass2db --job N --lang de -> same for rows already stored in the DB with a >40% piece
# ---------------------------------------------------------------------------
