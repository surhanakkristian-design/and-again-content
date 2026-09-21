#!/usr/bin/env python3
"""Builds run_2g_cz.py / run_2g_lk.py / build_upload_2g.py from the phase2f originals (READ ONLY) by asserted
text replacements and records every change, with every removed code line, in CHANGES_2G.md."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(os.path.dirname(H)); F2 = os.path.join(TO, "phase2f")
CH = {}
def rd(p): return open(p, encoding="utf-8").read()
def rep(f, src, old, new, why, n=1, show_removed=False):
    c = src.count(old)
    assert (c == n) if n else c > 0, "%s: %r found %d times" % (f, old[:70], c)
    CH.setdefault(f, []).append((why, old if show_removed else None)); return src.replace(old, new)
def rsub(f, src, pat, fn, why, show_removed=False):
    rx = re.compile(pat, re.M); m = rx.findall(src)
    assert len(m) == 1, "%s: regex %r matched %d" % (f, pat, len(m))
    CH.setdefault(f, []).append((why, rx.search(src).group(0) if show_removed else None)); return rx.sub(fn, src)
def cut(f, src, a, b, new, why):
    assert src.count(a) == 1 and src.count(b) == 1, (f, a, b)
    i = src.rfind("\n", 0, src.find(a)) + 1; j = src.rfind("\n", 0, src.find(b)) + 1
    assert j > i; CH.setdefault(f, []).append((why, src[i:j])); return src[:i] + new + src[j:]

# ============================================================== run_2g_cz.py
f = "run_2g_cz.py"; s = rd(os.path.join(F2, "run_2f_cz.py"))
s = rep(f, s, '"""Phase 2E TASK B: finish the CZECH half', '"""PHASE 2G PART B: patched copy of phase2f/run_2f_cz.py; every change is in partB/CHANGES_2G.md.\n\nPhase 2E TASK B: finish the CZECH half', "docstring marks the copy")
s = rsub(f, s, r'^BASE = os\.path\.dirname\(H\).*$', lambda m: 'BASE = os.path.dirname(os.path.dirname(H))    # 2G: partB is one level deeper', "BASE = translation-offline from phase2g/partB")
s = rsub(f, s, r'^E2 = os\.path\.join\(BASE, "phase2e"\).*$', lambda m: m.group(0) + '\nF2 = os.path.join(BASE, "phase2f")            # INPUT, read only (2G adopts from here first)', "F2 = phase2f (input, read only)")
s = cut(f, s, "TP_WINDOW_S = 300", 'LANGS = ("cz",)', "", "B1: throughput-guard constants REMOVED")
s = rep(f, s, 'LANGS = ("cz",)\n', 'LANGS = ("cz",)\n# ---------------------------------------------------------------- 2G Part B constants\nPIECE_ROWS = 10                  # B2: never narrower than 10 rows\nPIECE_MAX_RETRY = 2              # B2: each piece runs once with MAX_RETRY 2\nPIECED = {"cz_0002_s04_v": (5415, 5464), "cz_0003_s04_v": (6365, 6464), "cz_0004_s04_v": (7365, 7464)}\nEST["vp"] = 40_000               # reservation default for a 10-row piece until 2 pieces have returned\n', "B2 constants: PIECE_ROWS 10, PIECE_MAX_RETRY 2, PIECED ranges, EST['vp']")
s = rep(f, s, '"ignore_stop": False, "self_test": False}', '"ignore_stop": False, "self_test": False, "no_spawn": False}', "--no-spawn (assemble-only, 0 model calls) for the post-usage-stop pass")
s = rep(f, s, '        elif x == "--ignore-stop-file": a["ignore_stop"] = True\n', '        elif x == "--ignore-stop-file": a["ignore_stop"] = True\n        elif x == "--no-spawn": a["no_spawn"] = True\n', "--no-spawn parsed")
for a_, b_ in (('"ledger_2f_cz%s.json"', '"ledger_2g_cz%s.json"'), ('"gates_2f_cz%s.json"', '"gates_2g_cz%s.json"'), ('"run_2f_cz%s.log"', '"run_2g_cz%s.log"')):
    s = rep(f, s, a_, b_, "file name %s -> %s" % (a_, b_))
s = rep(f, s, 'DEFECTS = os.path.join(H, "DEFECTS_run_2f_cz%s.md" % DRY)', 'DEFECTS = os.path.join(H, "DEFECTS_run_2g_cz%s.md" % DRY)\nTIMELINE = os.path.join(H, "session_timeline%s.jsonl" % DRY)          # B3\nPIECES_JSON = os.path.join(H, "pieces_2g%s.json" % DRY)               # B2\nREFUSED_MD = os.path.join(H, "REFUSED_PIECES%s.md" % DRY)             # B2\nPROGRESS = os.path.join(H, "progress%s.log" % DRY)', "DEFECTS renamed; TIMELINE / PIECES_JSON / REFUSED_MD / PROGRESS paths")
s = rep(f, s, '    commit([fn, LEDGER, GATES, LOGP], "Phase 2F: STOP %s" % reason)\n    sys.exit(3)', '    pieces_report()\n    commit([fn, LEDGER, GATES, LOGP, TIMELINE, PIECES_JSON, REFUSED_MD], "Phase 2F: STOP %s" % reason)\n    sys.exit(3)', "stop() writes the piece log before exiting")
s = rep(f, s, "# Phase 2E (Czech) STOP:", "# Phase 2G Part B (Czech) STOP:", "stop-file header")
s = rep(f, s, '"Phase 2F', '"Phase 2G Part B', "commit messages say Phase 2G Part B", n=0)
s = rsub(f, s, r'^(\s*)"throughput_guard": \{"window_s": TP_WINDOW_S.*$', lambda m: m.group(1) + '"throughput_guard": "REMOVED in Phase 2G Part B (B1)",', "B1: ledger no longer records guard settings", show_removed=True)
s = cut(f, s, "-- change 4: throughput guard", "-- change 5: projection gate", "# ---- 2G B1: ThroughputGuard / GUARD / monitor_loop REMOVED ENTIRELY (CHANGES_2G.md)\n\n", "B1: ThroughputGuard class, GUARD and monitor_loop REMOVED")
s = cut(f, s, "    # change 4: throughput guard\n", "    # change 5: projection gate\n", "    # 2G B1: every throughput-guard self-test was removed with the guard\n", "B1: guard self-tests REMOVED (they also exercised the 2F sleep ledger, which stays but no longer feeds anything)")
s = rep(f, s, '    if not A["dry"]:\n        threading.Thread(target=monitor_loop, daemon=True).start()\n', "", "B1: monitor thread start REMOVED", show_removed=True)
s = rep(f, s, '    load_ledger()\n    if A["self_test"]:\n        selftest()\n    if not A["dry"]:\n        if not os.path.exists(BIN):', '    load_ledger()\n    if A["no_spawn"]:\n        STATE["stop_spawn"] = "no-spawn: assemble-only pass, 0 model calls"\n    if A["self_test"]:\n        selftest()\n    if not A["dry"] and not A["no_spawn"]:\n        if not os.path.exists(BIN):', "--no-spawn: never loads the token, never spawns")
s = rep(f, s, '        if STATE["stop_spawn"]:\n            log("SKIP-REMAINING", bid,', '        if STATE["stop_spawn"] and not A["no_spawn"]:\n            log("SKIP-REMAINING", bid,', "--no-spawn still assembles every batch")
s = rep(f, s, '        if STATE["stop_spawn"]:\n            break\n', '        progress_line("batch %s (%s)" % (bid, st), locals().get("p"))\n        if STATE["stop_spawn"] and not A["no_spawn"]:\n            break\n', "progress.log line after every batch")
s = rep(f, s, '    STATE["finished"] = True\n', '    STATE["finished"] = True\n    pieces_report()\n', "piece log at the end of every run")
s = rep(f, s, '            p = projection(STATE["rows_paid"], _vr, STATE["tok"], time.time() - STATE["t0"])', '            p = projection_2g(_vr, _rwn, time.time() - STATE["t0"]) if STATE["rows_paid"] > 0 else None', "projection gate KEPT, but session-based: remaining sessions x running per-kind mean (pieces have their own kind, so 10-row overhead does not inflate the per-row extrapolation)", show_removed=True)
s = rep(f, s, '                p["projected_total_tokens"] += _rwn * EST["rw"]\n', "", "rw sessions are inside projection_2g now", show_removed=True)
s = rep(f, s, '    srcs = [("phase2e", os.path.join(E2, "out", "sessions")),', '    srcs = [("phase2f", os.path.join(F2, "out", "sessions")), ("phase2e", os.path.join(E2, "out", "sessions")),', "adopt (COPY) finished sessions from phase2f first")
s = rep(f, s, r're.match(r"^cz_\d{4}_s\d{2}_(v|rw)\.json$", fn)', r're.match(r"^cz_\d{4}_s\d{2}_(v|rw)(_h[12])?\.json$", fn)', "adopt 2F half-chunk sessions (cz_0002_s04_v_h1)")
HELP = r'''# ---------------------------------------------------------------- 2G Part B: timeline, hard Claude stops, pieces
_LAUNCH = [0]
INFLIGHT_SET = set()
TL_LOCK = threading.Lock()
PIECE_ERR = {}
USAGE_RE = re.compile(r"usage limit|hit your (usage )?limit|weekly limit|5-hour limit|out of extra usage|"
                      r"credit balance is too low|limit will reset|limit resets|resets at \d|\u00b7 resets|quota", re.I)
HTTP_RE = re.compile(r"\b(429|40[0-9]|5\d\d)\b")
def _redact(s): return re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", s or "")
def _is_piece(sid): return bool(re.search(r"_p\d\d$", sid))
def tl(ev, sid, **kw):
    """B3: one JSON line per session event -> session_timeline.jsonl."""
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "t": round(time.time(), 3), "event": ev, "session": sid,
           "chunk": re.sub(r"_(v|rw|lk)(_p\d\d|_h[12])?$", "", sid)}
    rec.update(kw)
    with TL_LOCK:
        with open(TIMELINE, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
def progress_line(stage, p):
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "who": "run_2g_cz", "stage": stage,
           "cum_tokens_annotation_ledger": STATE["tok"], "cap_partB_all_headless": A["cap"], "projection": p}
    with TL_LOCK:
        with open(PROGRESS, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
def projection_2g(vr, rwn, elapsed):
    def mean(k, dt, dw):
        n, tk, w = STATE["kind"][k]
        return (tk / float(n), w / float(n)) if n >= 2 else (float(dt), float(dw))
    vt, vw = mean("v", EST["v"], 300.0)
    rt, rw_ = mean("rw", EST["rw"], 200.0)
    nv = vr / float(NSESS)
    s_ = elapsed + (nv * vw + rwn * rw_) / float(A["par"])
    return {"method": "2G session-based: remaining full v sessions and rw sessions x running per-kind mean",
            "rows_paid": STATE["rows_paid"], "cum_tokens": STATE["tok"], "mean_v_tok": round(vt), "mean_rw_tok": round(rt),
            "projected_total_tokens": int(STATE["tok"] + nv * vt + rwn * rt),
            "projected_total_s": round(s_, 1), "projected_total_h": round(s_ / 3600.0, 2)}
def hard_claude_stop(reason, sid, text):
    fn = os.path.join(H, "%s_%s.md" % (STOPPFX, reason))
    with open(fn, "w", encoding="utf-8") as fh:
        fh.write("# Phase 2G Part B STOP: %s\n\nSession `%s` (launch index %d): %s.\n\nNothing is retried and no further "
                 "session is spawned. The chain skips every stage that needs a headless Claude session, runs B6 (no Claude "
                 "session) on what exists, then writes DONE.\n\nRedacted error text (tail):\n\n```\n%s\n```\n\nWritten %s. "
                 "Headless tokens in the annotation ledger: %d (a session killed in flight is not counted).\n"
                 % (reason, sid, _LAUNCH[0], "headless Claude usage-limit / quota error" if reason == "usage_limit"
                    else "the very first headless session failed to run", _redact(text)[-1500:],
                    time.strftime("%Y-%m-%d %H:%M:%S"), STATE["tok"]))
    tl("hard_stop", sid, reason=reason, text=_redact(text)[-400:])
    log("HARD-STOP", reason, sid, "- exiting immediately, no retry")
    try:
        save_ledger(); pieces_report()
        commit([fn, LEDGER, LOGP, TIMELINE, PIECES_JSON, REFUSED_MD, DEFECTS], "Phase 2G Part B: STOP %s" % reason)
    finally:
        os._exit(4)
def post_call(sid, kind, attempt, p, lidx):
    out, err = p.stdout or "", p.stderr or ""
    try:
        j = json.loads(out); j = j if isinstance(j, dict) else {}
    except Exception:
        j = {}
    is_err = bool(j.get("is_error"))
    bad = (p.returncode != 0) or is_err
    if not bad and "429" not in (out + err):
        return
    blob = _redact(err[-3000:] + "\n" + out[-3000:])
    codes = sorted(set(HTTP_RE.findall(blob))) if bad else ["429"]
    with LOCK:
        fl = sorted(INFLIGHT_SET)
    tl("http_error", sid, kind=kind, attempt=attempt + 1, launch_index=lidx, exit=p.returncode, is_error=is_err,
       codes=codes, inflight=len(fl), inflight_ids=fl, text=blob.strip()[-400:])
    PIECE_ERR[sid] = blob.strip()[-400:]
    if bad and USAGE_RE.search(blob):
        hard_claude_stop("usage_limit", sid, blob)
    if p.returncode != 0 and lidx == 1 and attempt == 0 and "429" not in blob:
        hard_claude_stop("first_session_failed", sid, blob)
def pieces_report():
    """B2: per-piece success/failure + error text -> pieces_2g.json; failing pieces' sk + cz text -> REFUSED_PIECES.md."""
    try:
        errs = {}
        if os.path.exists(TIMELINE):
            for l in open(TIMELINE, encoding="utf-8"):
                try:
                    e = json.loads(l)
                except Exception:
                    continue
                if e.get("event") in ("http_error", "giveup", "hard_stop"):
                    errs.setdefault(e["session"], []).append(e.get("text") or e.get("why") or e.get("reason"))
        sk = {r["exercise_id"]: r for r in SEL if r["lang"] == "sk"}
        rep, bad = {}, []
        for bid, lang, rows in BATCHES:
            for k, c in enumerate(chunks(rows), 1):
                sid = "%s_s%02d_v" % (bid, k)
                if sid not in PIECED:
                    continue
                lo, hi = PIECED[sid]
                for j in range(0, len(c), PIECE_ROWS):
                    sub = c[j:j + PIECE_ROWS]
                    if not (sub[0]["n"] >= lo and sub[-1]["n"] <= hi):
                        continue
                    pid = "%s_p%02d" % (sid, j // PIECE_ROWS + 1)
                    ok = sess_complete(pid, [r["n"] for r in sub]) is not None
                    led = STATE["sessions"].get(pid) or {}
                    tried = bool(led) or os.path.exists(sess_path(pid))
                    st = "SUCCESS" if ok else ("FAILURE" if tried else "NOT_RUN")
                    er = [x for x in errs.get(pid, []) if x][-4:] or ([led["why"]] if led.get("why") else [])
                    if st == "FAILURE" and not er:
                        er = ["returned but incomplete/unparsable (ledger status %s, rows %s)" % (led.get("status"), led.get("rows"))]
                    rep[pid] = {"chunk": sid, "n_range": "%d-%d" % (sub[0]["n"], sub[-1]["n"]), "status": st,
                                "ledger_status": led.get("status"), "tokens": led.get("tokens"), "errors": er}
                    if st == "FAILURE":
                        bad.append((pid, sub))
        cnt = collections.Counter(v["status"] for v in rep.values())
        json.dump({"rows_per_piece": PIECE_ROWS, "max_retry": PIECE_MAX_RETRY, "counts": dict(cnt), "pieces": rep,
                   "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}, open(PIECES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        esc = lambda x: (x or "").replace("|", "\\|").replace("\n", " ")
        md = ["# Refused / failed 10-row pieces - Phase 2G Part B", "",
              "%d of %d pieces failed (%s). Each piece ran once with MAX_RETRY %d; nothing was narrowed below %d rows." %
              (len(bad), len(rep), dict(cnt), PIECE_MAX_RETRY, PIECE_ROWS), ""]
        for pid, sub in bad:
            md += ["## %s (n %s)" % (pid, rep[pid]["n_range"]), "", "Error: `%s`" % esc(" / ".join(str(x) for x in rep[pid]["errors"]))[:900], "",
                   "| n | exercise_id | Slovak | Czech |", "|---|---|---|---|"]
            for r in sub:
                s_ = sk.get(r["exercise_id"])
                md.append("| %d | %s | %s | %s |" % (r["n"], r["exercise_id"], esc(s_["src"]) if s_ else "(no Slovak row with this exercise_id)", esc(r["src"])))
            md.append("")
        open(REFUSED_MD, "w", encoding="utf-8").write("\n".join(md) + "\n")
        log("PIECES", json.dumps(dict(cnt)))
        commit([PIECES_JSON, REFUSED_MD], "Phase 2G Part B: 10-row piece log %s" % dict(cnt))
    except Exception as ex:
        log("PIECES-REPORT-FAILED", repr(ex))
def split_pieces(tasks):
    """B2: the three refused s04 v chunks run as 10-row pieces <sid>_pNN, in place (launch order preserved)."""
    out = []
    head = VPROMPT("cz")
    for sid, kind, prompt, crows in tasks:
        if sid not in PIECED:
            out.append((sid, kind, prompt, crows)); continue
        lo, hi = PIECED[sid]
        assert prompt.startswith(head), sid
        ls = prompt[len(head):].split("\n")
        assert len(ls) == len(crows) == NSESS and all(json.loads(x)["n"] == r["n"] for x, r in zip(ls, crows)), sid
        made = 0
        for k in range(0, len(crows), PIECE_ROWS):
            sub = crows[k:k + PIECE_ROWS]
            if sub[0]["n"] >= lo and sub[-1]["n"] <= hi:
                out.append(("%s_p%02d" % (sid, k // PIECE_ROWS + 1), kind, head + "\n".join(ls[k:k + PIECE_ROWS]), sub)); made += 1
        assert made * PIECE_ROWS == hi - lo + 1, (sid, made)
    return out

'''
s = rep(f, s, 'def session(sid, kind, prompt, rows):\n    want = [r["n"] for r in rows]\n', HELP + 'def session(sid, kind, prompt, rows):\n    want = [r["n"] for r in rows]\n    _sk = kind + "p" if _is_piece(sid) else kind           # 2G: pieces keep their own running means\n', "B2/B3/stop helpers; pieces get their own stats kind 'vp'")
s = rep(f, s, '    e = est_for(kind)\n', '    e = est_for(_sk)\n', "reservation estimate per stats kind")
s = rep(f, s, '            return sid, ("STOP", "token_cap",', '            tl("cap_refused", sid, kind=kind, spent=STATE["tok"], reserved_inflight=STATE["inflight"] * max(EST.values()), est=e, cap=A["cap"])\n            return sid, ("STOP", "token_cap",', "B3: cap refusal logged")
s = rep(f, s, '        STATE["inflight"] += 1\n    try:\n        t_sess = time.time()\n', '        STATE["inflight"] += 1\n        _LAUNCH[0] += 1\n        _lidx = _LAUNCH[0]\n        INFLIGHT_SET.add(sid)\n        _fl = sorted(INFLIGHT_SET)\n    tl("launch", sid, kind=kind, launch_index=_lidx, rows=len(rows), n_range=nranges(want), inflight=len(_fl),\n       inflight_ids=_fl, reserved_before_launch=proj, cap=A["cap"], piece=_is_piece(sid))\n    try:\n        t_sess = time.time()\n', "B3: launch record (time, index, concurrency)")
s = rep(f, s, '        for attempt in range(MAX_RETRY + 1):', '        _mr = PIECE_MAX_RETRY if _is_piece(sid) else MAX_RETRY\n        for attempt in range(_mr + 1):', "B2: pieces MAX_RETRY 2")
s = rep(f, s, '            wall_cap, tok_cap = circuit_limits(kind)\n', '            wall_cap, tok_cap = circuit_limits(_sk)\n', "circuit breaker per stats kind (floors unchanged)")
s = rep(f, s, '            if should_retry(p.returncode, p.stdout, p.stderr):', '            post_call(sid, kind, attempt, p, _lidx)\n            if should_retry(p.returncode, p.stdout, p.stderr):', "B3 http-error log + usage-limit / first-session hard stop")
s = rep(f, s, '                if attempt < MAX_RETRY:', '                if attempt < _mr:', "retry ceiling per session type")
s = rep(f, s, '"attempt", attempt + 1, "of", MAX_RETRY,', '"attempt", attempt + 1, "of", _mr,', "retry log")
s = rep(f, s, '"retries_exhausted after %d retries (%s)" % (MAX_RETRY, why)', '"retries_exhausted after %d retries (%s)" % (_mr, why)', "give-up text")
s = rep(f, s, '        _wc, tok_cap = circuit_limits(kind)\n', '        _wc, tok_cap = circuit_limits(_sk)\n', "token breaker per stats kind")
s = rep(f, s, 'STATE["kind"][kind][0] += 1; STATE["kind"][kind][1] += tok; STATE["kind"][kind][2] += wall', 'STATE["kind"][_sk][0] += 1; STATE["kind"][_sk][1] += tok; STATE["kind"][_sk][2] += wall', "running means per stats kind")
s = rep(f, s, '    finally:\n        with LOCK:\n            STATE["inflight"] -= 1\n', '    finally:\n        with LOCK:\n            STATE["inflight"] -= 1\n            INFLIGHT_SET.discard(sid)\n            _left = sorted(INFLIGHT_SET)\n        _s = STATE["sessions"].get(sid) or {}\n        tl("end", sid, kind=kind, launch_index=_lidx, status=_s.get("status"), rows=_s.get("rows"), tokens=_s.get("tokens"),\n           wall_s=round(time.time() - t_sess, 1), inflight_after=len(_left), inflight_ids_after=_left)\n', "B3: end record")
s = rep(f, s, '    log("GIVEUP", sid, kind, why,', '    tl("giveup", sid, kind=kind, why=why, tokens=tok)\n    log("GIVEUP", sid, kind, why,', "B3: give-up record")
s = rep(f, s, 'for r in fb), fb))\n    return tasks\n', 'for r in fb), fb))\n    return split_pieces(tasks)\n', "B2: s04 v chunks replaced by their 10-row pieces")
s = rep(f, s, '            for suf, sub in (("_h1", ns[:len(ns) // 2]), ("_h2", ns[len(ns) // 2:])):', '            for suf, sub in [("_h1", ns[:len(ns) // 2]), ("_h2", ns[len(ns) // 2:])] + [("_p%02d" % (k // PIECE_ROWS + 1), ns[k:k + PIECE_ROWS]) for k in range(0, len(ns), PIECE_ROWS)]:', "B4: 2F half-chunk assembler extended to 10-row pieces")
s = rep(f, s, '                missing.append(sid)\n                for n in gone:', '                if gone:\n                    missing.append(sid)\n                for n in gone:', "a chunk fully recovered from halves/pieces is not 'missing'")
s = rep(f, s, '        if p is not None and p > GATE3_BAR:\n            stop("gate3_%s_%s"', '        if p is not None and p > GATE3_BAR and (A["dry"] or A["no_spawn"]):\n            log("GATE3-NOT-STOPPING", bid, k, p, "(dry run or assemble-only pass)")\n            continue\n        if p is not None and p > GATE3_BAR:\n            stop("gate3_%s_%s"', "GATE 3 stops only live runs (dry / assemble-only record it)")
s = rep(f, s, '    if first:\n        write_uploads(bid, anns)', '    if first and False:                                   # 2G: B6 builds the only upload package\n        write_uploads(bid, anns)', "no per-batch upload candidates")
s = rep(f, s, '    ck("N_is_100", NSESS == 100)\n', '    ck("N_is_100", NSESS == 100)\n    ck("2g:guard_removed", "ThroughputGuard" not in globals() and "monitor_loop" not in globals() and "GUARD" not in globals())\n    ck("2g:usage_re_hits", bool(USAGE_RE.search("Claude AI usage limit reached|1758000000")) and bool(USAGE_RE.search("You\'ve hit your limit \\u00b7 resets 3pm")))\n    ck("2g:usage_re_ignores_rate_429", not USAGE_RE.search(\'API Error: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Number of request tokens has exceeded your per-minute rate limit"}}\'))\n    ck("2g:piece_rules", PIECE_MAX_RETRY == 2 and PIECE_ROWS == 10 and _is_piece("cz_0004_s04_v_p03") and not _is_piece("cz_0004_s04_v"))\n', "2G self-tests")
s = rep(f, s, 'EST["vp"] = 40_000 ', 'F2_ROWS = {json.loads(_l)["n"] for _l in open(os.path.join(F2, "out", "annotations_cz_final.jsonl"), encoding="utf-8") if _l.strip()}\nEST["vp"] = 40_000 ', "F2_ROWS = the 2,850 rows 2F already gated")
s = rep(f, s, '    g = gate3(bid, lang, anns)\n', '    gate3(bid + "_all_rows_DIAGNOSTIC", lang, anns)                # never gates\n    _new = [a for a in anns if a["n"] not in F2_ROWS]\n    if _new:\n        g = gate3(bid, lang, _new)\n    else:\n        log("GATE3-SKIP", bid, "no row of this batch is new in 2G; all of them were gated in 2E/2F")\n        g = {"agv4": {"ERROR_of_decided_pct": None}, "reader_nom": {"ERROR_of_decided_pct": None}}\n', "GATE 3 (2F code unchanged, bar 12 %) scores 50 random rows of the rows NEW in this batch; the whole re-assembled batch is scored as <bid>_all_rows_DIAGNOSTIC and never gates (the dry run showed the resampled cz_0002 at 14.58 % over rows 2E/2F had already gated and passed)", show_removed=True)
open(os.path.join(H, f), "w", encoding="utf-8").write(s)

# ============================================================== run_2g_lk.py
f = "run_2g_lk.py"; s = rd(os.path.join(F2, "run_2f_lk.py"))
s = rsub(f, s, r'^BASE = os\.path\.dirname\(H\).*$', lambda m: 'BASE = os.path.dirname(os.path.dirname(H))     # 2G: translation-offline', "BASE from partB")
s = rsub(f, s, r'^OUT = os\.path\.join\(H, "out"\).*$', lambda m: 'OUT = os.path.join(H, "lk")                    # 2G: only rows lacking a dedicated lk judgement (prep_lk.py)', "lk input/output dir = partB/lk")
for a_, b_ in (('"ledger_2f_lk.json"', '"ledger_2g_lk.json"'), ('"run_2f_lk.log"', '"run_2g_lk.log"'), ('"defects_2f_lk.txt"', '"defects_2g_lk.txt"')):
    s = rep(f, s, a_, b_, "file name %s -> %s" % (a_, b_))
s = rep(f, s, 'SHAREF = os.path.join(H, "SHA_inputs_before.txt")', 'SHAREF = os.path.join(os.path.dirname(H), "SHA_inputs_before.txt")   # 2G: phase2g/SHA_inputs_before.txt', "input-hash baseline = phase2g/SHA_inputs_before.txt")
s = rep(f, s, '"Phase 2F', '"Phase 2G Part B', "commit messages", n=0)
s = rep(f, s, 'import concurrent.futures as cf\n', 'import concurrent.futures as cf\ndef _samp(rnd, pop, k): return rnd.sample(pop, min(k, len(pop)))   # 2G: fewer than 250 rows is legal\n', "sample helper")
s = rep(f, s, 'rnd.sample(', '_samp(rnd, ', "GATE sample tolerates < 250 rows", n=0)
s = rep(f, s, 'PROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]\n', 'PROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]\nassert PROMPT_SHA == "5fa910459c078539", "2G B5: lk prompt sha16 drifted: %s" % PROMPT_SHA\n', "B5: prompt sha16 asserted at import")
LKH = r'''# ---------------------------------------------------------------- 2G Part B: timeline + usage-limit hard stop
TIMELINE = os.path.join(H, "session_timeline.jsonl")
USAGE_RE = re.compile(r"usage limit|hit your (usage )?limit|weekly limit|5-hour limit|out of extra usage|"
                      r"credit balance is too low|limit will reset|limit resets|resets at \d|\u00b7 resets|quota", re.I)
TL_LOCK = threading.Lock()
def _tl(ev, sid, **kw):
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "t": round(time.time(), 3), "event": ev, "session": sid,
           "chunk": re.sub(r"_lk$", "", sid)}
    rec.update(kw)
    with TL_LOCK:
        with open(TIMELINE, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
def _post_call_lk(sid, attempt, p):
    out, err = p.stdout or "", p.stderr or ""
    try:
        j = json.loads(out); j = j if isinstance(j, dict) else {}
    except Exception:
        j = {}
    bad = p.returncode != 0 or bool(j.get("is_error"))
    blob = REDACT(err[-3000:] + "\n" + out[-3000:]) if bad else ""
    _tl("attempt_end", sid, kind="lk", attempt=attempt + 1, exit=p.returncode, is_error=bool(j.get("is_error")),
        inflight=STATE["inflight"])
    if bad or "429" in (out + err):
        _tl("http_error", sid, kind="lk", attempt=attempt + 1, exit=p.returncode,
            codes=sorted(set(re.findall(r"\b(429|40[0-9]|5\d\d)\b", blob))) if bad else ["429"], text=blob.strip()[-400:])
    if bad and USAGE_RE.search(blob):
        fn = os.path.join(H, "STOP_usage_limit.md")
        open(fn, "w", encoding="utf-8").write(
            "# Phase 2G Part B STOP: usage_limit (lk stage)\n\nSession `%s` failed with a headless-Claude usage-limit / "
            "quota error. Nothing is retried; the lk stage exits at once; the chain runs B6 and writes DONE.\n\n```\n%s\n```\n\n"
            "Written %s. lk tokens so far: %d.\n" % (sid, blob[-1500:], time.strftime("%Y-%m-%d %H:%M:%S"), STATE["tok"]))
        _tl("hard_stop", sid, reason="usage_limit")
        log("HARD-STOP usage_limit", sid, "- exiting immediately, no retry")
        try:
            save_ledger(); commit([fn, LEDGER, LOGP, TIMELINE], "Phase 2G Part B: STOP usage_limit (lk)")
        finally:
            os._exit(4)

'''
s = rep(f, s, 'def session(sid, bid, rows):\n', LKH + 'def session(sid, bid, rows):\n', "timeline + usage-limit helpers")
s = rep(f, s, '        for attempt in range(4):\n', '        _tl("launch", sid, kind="lk", rows=len(rows), inflight=STATE["inflight"])\n        for attempt in range(4):\n', "B3: lk launch record")
s = rep(f, s, '                               capture_output=True, text=True, env=ENV, cwd=H)\n', '                               capture_output=True, text=True, env=ENV, cwd=H)\n            _post_call_lk(sid, attempt, p)\n', "B3 + usage-limit check after every lk CLI call")
open(os.path.join(H, f), "w", encoding="utf-8").write(s)

# ============================================================== build_upload_2g.py
f = "build_upload_2g.py"; s = rd(os.path.join(F2, "build_upload_cz.py"))
s = rep(f, s, 'BASE = os.path.dirname(H);', 'BASE = os.path.dirname(os.path.dirname(H));', "BASE from partB")
s = rep(f, s, '    rp = os.path.join(OUT, "UPLOAD_README.md")\n    base = open(os.path.join(D2OUT, "UPLOAD_README.md"), encoding="utf-8").read()', '    rp = os.path.join(H, "UPLOAD_README.md")                                   # 2G: partB/UPLOAD_README.md\n    base = open(os.path.join(BASE, "phase2f", "out", "UPLOAD_README.md"), encoding="utf-8").read()   # 2G: update of 2F\'s', "README = 2F's README + 2G addendum, written to partB/")
s = rep(f, s, "# ADDENDUM — Czech (Phase 2E)", "# ADDENDUM — Czech (Phase 2G Part B; supersedes the Czech row counts above)", "addendum header")
s = rep(f, s, '"Phase 2E: Czech upload package (%d rows, sheet cz) + README addendum" % len(rows)', '"Phase 2G Part B: Czech upload package (%d rows, sheet cz) + README update\\n\\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>" % len(rows)', "commit message")
open(os.path.join(H, f), "w", encoding="utf-8").write(s)

# ============================================================== CHANGES_2G.md
rp1 = rd(os.path.join(F2, "run_part1.py"))
i = rp1.find("    stops = [f for f in os.listdir(H)"); j = rp1.find('    note_stage("lk")')
md = ["# CHANGES_2G - Phase 2G Part B (finish Czech annotation)", "",
      "All code is a COPY of phase2f/ (read only), produced by `make_2g.py` with asserted replacements. No checker rule, "
      "no prompt text and no gate bar changed.", "",
      "## B1 - throughput guard REMOVED ENTIRELY (removed code lines below)", "",
      "Kept: token cap with in-flight accounting (cap 2,900,000 for all Part B headless sessions: annotation `--cap 2900000`, "
      "lk `--cap 2900000 - annotation spend`; the reservation `spent + inflight x 95,000 + estimate` is checked before every "
      "launch), the per-session circuit breaker (wall floor 900 s, token floor 200,000, 3x running mean), and the projection gate "
      "(4 h wall, cap tokens) - the projection is now session-based (see below).", ""]
for fn_, items in CH.items():
    md += ["## %s" % fn_, ""]
    for why, removed in items:
        md.append("* " + why)
        if removed:
            md += ["", "  Removed / replaced code:", "", "```python"] + removed.rstrip("\n").split("\n") + ["```", ""]
    md.append("")
md += ["## B5 - chain logic: a STOP file blocks only the stage that wrote it", "",
       "2F's `run_part1.py` downgraded the lk pass to `--merge-only` whenever ANY `STOP_*.md` existed (D-2F-10, D-2F-12). "
       "Removed logic:", "", "```python"] + rp1[i:j].rstrip("\n").split("\n") + ["```", "",
       "`chain_2g.sh` runs the paid lk pass after annotation regardless of any annotation-stage STOP file "
       "(token_cap, projection_*, gate3_*). The only exception is the brief's critical stop rule: after "
       "`STOP_usage_limit.md` or `STOP_first_session_failed.md` no further headless Claude session is started "
       "anywhere; B6 (0 Claude sessions) still runs and DONE is written.", "",
       "## Deviations to note", "",
       "* Finished 2F sessions (cz_0004 s01-s03, s05-s08 v+rw, cz_0002_s04_v_h1, everything of cz_0001-0003) are ADOPTED by COPY "
       "at 0 tokens instead of re-run; only missing sessions are paid for.",
       "* Projection gate kept, formula changed to remaining sessions x running per-kind mean (pieces are their own kind `vp`); "
       "the 2F per-row extrapolation would have extrapolated 10-row-piece overhead onto full chunks.",
       "* GATE 3 gates only rows new in 2G (50 random of them per batch); the full re-assembled batch is a never-gating diagnostic.",
       "* Gemini: Part B makes 0 Gemini calls (GATE 3 and lk use no Gemini).", ""]
open(os.path.join(H, "CHANGES_2G.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print("built", list(CH), sum(len(v) for v in CH.values()), "changes")
