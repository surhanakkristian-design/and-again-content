#!/usr/bin/env python3
"""Phase 2F PART 1 — one unattended driver.  Adopt -> annotate what is missing -> dedicated lk pass over
the NEW rows -> regenerate annotations_cz_final.jsonl + upload_cz_final.xlsx.  Uploads NOTHING, writes
NOTHING to the database, never pushes.  Tripwire: 2,000,000 headless tokens for Part 1's own spend.
Writes PART1_DONE (one-line status) when it finishes or stops, and PART1_STOP.md if it stops early."""
import json, os, re, shutil, subprocess, sys, time

H = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(H); REPO = os.path.dirname(BASE)
E2 = os.path.join(BASE, "phase2e"); C2 = os.path.join(BASE, "phase2c")
OUT = os.path.join(H, "out"); SESS = os.path.join(OUT, "sessions"); DIAG = os.path.join(H, "diag")
os.makedirs(SESS, exist_ok=True)
TRIPWIRE = 2_000_000
TARGET_ROWS = 4064
ADOPTED_ROWS = 2800
LOGP = os.path.join(H, "run_part1.log")
LOG = open(LOGP, "a", buffering=1, encoding="utf-8")
def log(*a):
    s = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(x) for x in a)
    LOG.write(s + "\n"); print(s, flush=True)
def git(paths, msg):
    try:
        subprocess.run(["git", "-C", REPO, "add", "-A", "translation-offline/phase2f"], capture_output=True)
        subprocess.run(["git", "-C", REPO, "commit", "-q", "-m",
                        msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>"], capture_output=True)
    except Exception as e:
        log("GIT-FAIL", type(e).__name__, str(e)[:120])
def ledger_spend(p):
    try:
        return int(json.load(open(p, encoding="utf-8")).get("spent") or 0)
    except Exception:
        return 0
CZL = os.path.join(H, "ledger_2f_cz.json"); LKL = os.path.join(H, "ledger_2f_lk.json")
def spend(): return ledger_spend(CZL) + ledger_spend(LKL)
def rows_present():
    n = 0
    for f in sorted(os.listdir(OUT)):
        if re.match(r"^annotations_cz_\d{4}\.jsonl$", f):
            n += sum(1 for l in open(os.path.join(OUT, f), encoding="utf-8") if l.strip())
    return n
def note_stage(stage):
    """§1.3.5: cumulative headless tokens + the projected total, into both ledgers and the log."""
    cum, pres = spend(), rows_present()
    new = max(0, pres - ADOPTED_ROWS)
    tpr = (cum / new) if new else None
    proj = int(cum + tpr * max(0, TARGET_ROWS - pres)) if tpr else None
    rec = {"stage": stage, "at": time.strftime("%Y-%m-%dT%H:%M:%S"), "cumulative_headless_tokens": cum,
           "rows_present": pres, "new_rows_paid_for_in_2F": new,
           "tok_per_new_row": round(tpr, 1) if tpr else None, "projected_part1_total_tokens": proj,
           "tripwire": TRIPWIRE}
    for p in (CZL, LKL):
        try:
            d = json.load(open(p, encoding="utf-8"))
            d.setdefault("part1_stages", []).append(rec)
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        except Exception:
            pass
    log("LEDGER-STAGE", json.dumps(rec))
    return rec
def finish(status, stop_md=None):
    sp = os.path.join(H, "PART1_STOP.md")
    if stop_md:
        open(sp, "w", encoding="utf-8").write(stop_md)
    elif os.path.exists(sp):
        os.remove(sp)                                  # this run did NOT stop early: the old record goes
        log("PART1_STOP-REMOVED", "previous stop record deleted; this run did not stop early")
    open(os.path.join(H, "PART1_DONE"), "w", encoding="utf-8").write(status.strip() + "\n")
    log("PART1_DONE", status.strip())
    git(None, "Phase 2F Part 1: %s" % status.strip()[:70])
    # ---- LAST step, every outcome: hand back to Part 2's driver (resumable, writes PART2_RESULT.md)
    try:
        d2 = os.path.join(H, "p2")
        subprocess.Popen("nohup python3 p2_driver.py >> p2_driver.stdout.txt 2>&1 &", shell=True, cwd=d2)
        log("PART2-RELAUNCHED", "nohup python3 p2_driver.py in", d2)
    except Exception as e:
        log("PART2-RELAUNCH-FAILED", type(e).__name__, str(e)[:200])
    sys.exit(0)
def run(cmd, tag, cwd=H):
    log("RUN", tag, " ".join(cmd[:4]), "...")
    with open(os.path.join(H, "%s.stdout.txt" % tag), "a", encoding="utf-8") as f:
        rc = subprocess.run(cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT).returncode
    log("RUN-DONE", tag, "exit", rc)
    return rc

# ---------------------------------------------------------------- 1. adopt (COPY) with 2E's check
def vwant():
    rows = [json.loads(l) for l in open(os.path.join(C2, "selection_2c.jsonl"), encoding="utf-8") if l.strip()]
    cz = [r for r in rows if r["lang"] == "cz"]
    w = {}
    for i in range(0, len(cz), 1000):
        bid = "cz_%04d" % (i // 1000 + 1)
        b = cz[i:i + 1000]
        for k in range(0, len(b), 100):
            w["%s_s%02d_v" % (bid, k // 100 + 1)] = [r["n"] for r in b[k:k + 100]]
    return w
def adopt_v_rw():
    W, got, rej = vwant(), [], []
    src = os.path.join(E2, "out", "sessions")
    for fn in sorted(os.listdir(src)):
        if not re.match(r"^cz_\d{4}_s\d{2}_(v|rw)\.json$", fn):
            continue
        sid, sp = fn[:-5], os.path.join(src, fn)
        why = None
        try:
            d = json.load(open(sp, encoding="utf-8")); meta = d.get("meta") or {}
            if not isinstance(d.get("rows"), list):   why = "rows is not a list"
            elif meta.get("exit") != 0:               why = "exit %r" % meta.get("exit")
            elif not d["rows"]:                       why = "0 rows"
            elif sid in W and not set(W[sid]) <= {o.get("n") for o in d["rows"] if isinstance(o, dict)}:
                why = "does not cover its whole chunk"
        except Exception as e:
            why = "unparsable (%s)" % type(e).__name__
        if why:
            rej.append("%s: %s" % (sid, why)); log("ADOPT-REJECT", sid, why); continue
        dst = os.path.join(SESS, fn)
        if not os.path.exists(dst):
            shutil.copy2(sp, dst)                                  # COPY, never move
        got.append(sid); log("SKIP-DONE", sid, "adopted from phase2e (copied), 0 tokens")
    log("ADOPT", len(got), "v/rw sessions adopted,", len(rej), "rejected")
    return got, rej
def adopt_lk():
    """lk sessions are adopted ONLY where 2F's chunking gives the same rows: cz_0002/cz_0003 gain 100 rows
    each, which shifts every lk chunk boundary after s03, so those files are NOT reusable."""
    src = os.path.join(E2, "out", "sessions")
    want = {}
    for f in sorted(os.listdir(OUT)):
        mm = re.match(r"^annotations_(cz_\d{4})\.jsonl$", f)
        if not mm: continue
        ns = [json.loads(l)["n"] for l in open(os.path.join(OUT, f), encoding="utf-8") if l.strip()]
        for k in range(0, len(ns), 100):
            want["%s_s%02d_lk" % (mm.group(1), k // 100 + 1)] = ns[k:k + 100]
    got, rej = [], []
    for sid, ns in sorted(want.items()):
        sp = os.path.join(src, sid + ".json")
        if not os.path.exists(sp):
            continue
        try:
            d = json.load(open(sp, encoding="utf-8")); meta = d.get("meta") or {}
            ok = isinstance(d.get("rows"), list) and meta.get("exit") == 0 and \
                 set(ns) <= {o.get("n") for o in d["rows"] if isinstance(o, dict)}
        except Exception:
            ok = False
        if ok:
            if not os.path.exists(os.path.join(SESS, sid + ".json")):
                shutil.copy2(sp, os.path.join(SESS, sid + ".json"))
            got.append(sid); log("SKIP-DONE", sid, "lk adopted from phase2e (copied), 0 tokens")
        else:
            rej.append(sid); log("LK-NOT-ADOPTABLE", sid, "rows differ under 2F chunking or not complete -> re-run")
    log("ADOPT-LK", len(got), "adopted,", len(rej), "to re-run (these are the NEW rows)")
    return got, rej

def main():
    t0 = time.time()
    log("PART1-START", "tripwire", TRIPWIRE, "spend_so_far(diagnosis)", spend())
    adopt_v_rw(); note_stage("adopt"); git(None, "Phase 2F Part 1: adopted phase2e sessions (copied, 0 tokens)")

    # ------------------------------------------------ 2. the refused chunks, per the §1.2 ruling
    hp = os.path.join(DIAG, "halves_cz_0002_s04_v.json")
    halves_worked = False
    try:
        halves_worked = bool(json.load(open(hp, encoding="utf-8")).get("both_succeeded"))
    except Exception:
        log("HALVES", "no result file for cz_0002_s04_v")
    # 2F re-run: BOTH refused chunks are closed.  cz_0002_s04_v was refused nine times (its h2 four more);
    # cz_0003_s04_v already had its one whole-chunk attempt this phase and was refused.  Neither is
    # attempted again; this run annotates cz_0004 and cz_0005 and nothing else.
    exclude = ["cz_0002_s04_v", "cz_0003_s04_v"]
    ONLY_BATCHES = ("cz_0004", "cz_0005")
    log("RULING", "refused chunks closed:", exclude, "| this run runs only", ONLY_BATCHES,
        "| halves_worked(diagnosis)", halves_worked)
    note_stage("refused_chunks"); git(None, "Phase 2F Part 1: refused chunks handled per the §1.2 ruling")
    if spend() > TRIPWIRE:
        finish("STOPPED at the 2,000,000-token tripwire before the main annotation run (%d spent)" % spend(),
               "# PART 1 STOP\n\nThe tripwire fired before the main run; %d tokens spent.\n" % spend())

    # ------------------------------------------------ 3. annotate what is missing
    cap = max(0, TRIPWIRE - spend())
    cmd = [sys.executable, "run_2f_cz.py", "--all", "--cap", str(cap), "--ignore-stop-file"]
    if True:
        ids = json.loads(subprocess.run([sys.executable, "-c",
              "import sys,json;sys.path.insert(0,%r);import prompts_2f as P;"
              "m=P.load(['cz_0001','cz_0002','cz_0003','cz_0004','cz_0005']);"
              "out=[]\nfor b,l,r in m.BATCHES:\n out+= [t[0] for t in m.batch_tasks(b,l,r,m.derive_batch(r))]\n"
              "print(json.dumps(out))" % DIAG], capture_output=True, text=True, cwd=DIAG).stdout.splitlines()[-1])
        sel = [sid for sid in ids if sid not in exclude and sid.startswith(ONLY_BATCHES)]
        log("ONLY", len(sel), "session(s) may run:", ",".join(sel))
        for sid in sel:
            cmd += ["--only", sid]
    rc = run(cmd, "run_2f_cz")
    note_stage("annotate"); git(None, "Phase 2F Part 1: Czech annotation segment finished (exit %d)" % rc)
    stops = [f for f in os.listdir(H) if f.startswith("STOP_") and f.endswith(".md")]
    over = spend() > TRIPWIRE

    # ------------------------------------------------ 4. dedicated lk pass over the NEW rows only
    lk_rc = None
    if stops or over:
        log("LK-SKIPPED", "stop files", stops, "over_tripwire", over, "-> merge-only, no new tokens")
        adopt_lk()
        lk_rc = run([sys.executable, "run_2f_lk.py", "--merge-only"], "run_2f_lk")
    else:
        adopt_lk()
        lk_rc = run([sys.executable, "run_2f_lk.py", "--cap", str(max(0, TRIPWIRE - spend()))], "run_2f_lk")
    note_stage("lk"); git(None, "Phase 2F Part 1: dedicated lk pass (exit %s)" % lk_rc)

    # ------------------------------------------------ 5. CP comparison + upload package
    try:
        sys.argv = ["run_2f_lk.py", "--merge-only"]; sys.path.insert(0, H)
        import run_2f_lk as L
        rep = json.load(open(os.path.join(OUT, "REPORT_2f_lk.json"), encoding="utf-8"))
        po = rep["pooled"]
        k, n = po["k"], po["n"]
        pt, lo, hi = L.cp(k, n)
        md = ["# 2F lk pass — non-exact rate with exact 95 % Clopper-Pearson", "",
              "| set | k | n | non-exact %% | exact 95 %% CP |", "|---|---|---|---|---|",
              "| **2F pooled (all rows now present)** | %d | %d | %.2f | [%.2f, %.2f] |" % (k, n, pt, lo, hi),
              "| Czech pooled, 2E (2,700 judged) | 1416 | 2700 | 52.44 | [50.54, 54.34] |",
              "| Slovak, 1W / 2D | - | - | 51.13 | - |", "",
              "Span-adjusted leg: %.2f %% (k %s / n %s)." % (po.get("span_adjusted_pct", float("nan")),
                                                             po.get("span_k"), po.get("span_n")), "",
              "## Per session", "", "| session | non-exact % | k | n | exact 95 % CP |", "|---|---|---|---|---|"]
        for sid, v in sorted((rep.get("per_session") or {}).items()):
            kk = v.get("k") if v.get("k") is not None else v.get("adjust_or_unusable")
            nn = v.get("n") or v.get("judged")
            if kk is None or not nn:
                md.append("| %s | %s | - | - | - |" % (sid, v.get("pct"))); continue
            p3 = L.cp(kk, nn)
            md.append("| %s | %.2f | %d | %d | [%.2f, %.2f] |" % (sid, p3[0], kk, nn, p3[1], p3[2]))
        md += ["", "Sessions under 30 %% non-exact were re-run exactly once; attempt 1 is archived in "
               "`out/sessions_lowmode/` (see `low_mode` in REPORT_2f_lk.json).", ""]
        open(os.path.join(H, "REPORT_2f_lk_compare.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
        log("CP-COMPARE", "pooled %d/%d = %.2f %% [%.2f, %.2f] vs Czech 2E 52.44 [50.54, 54.34] vs Slovak 51.13"
            % (k, n, pt, lo, hi))
    except Exception as e:
        log("CP-COMPARE-FAILED", type(e).__name__, str(e)[:200])
        why = ("`out/REPORT_2f_lk.json` does not exist: the dedicated lk pass produced no report, which "
               "happens when there are NO NEW ROWS for it to judge."
               if isinstance(e, (IOError, OSError)) and not os.path.exists(os.path.join(OUT, "REPORT_2f_lk.json"))
               else "the lk report could not be read (%s: %s)." % (type(e).__name__, str(e)[:160]))
        open(os.path.join(H, "REPORT_2f_lk_compare.md"), "w", encoding="utf-8").write(
            "# 2F lk pass - non-exact rate with exact 95 %% Clopper-Pearson\n\n"
            "**No comparison could be computed.** %s\n\n"
            "Reference figures, unchanged: Czech pooled 2E 52.44 %% [50.54, 54.34] (1416/2700); "
            "Slovak 1W / 2D 51.13 %%.\n\nWritten %s.\n" % (why, time.strftime("%Y-%m-%dT%H:%M:%S")))
        log("CP-COMPARE", "degraded note written to REPORT_2f_lk_compare.md")
    run([sys.executable, "build_upload_cz.py"], "build_upload_cz")
    try:
        big = 0
        fin = os.path.join(OUT, "annotations_cz_final.jsonl")
        for l in open(fin, encoding="utf-8"):
            if l.strip():
                big = max(big, len(json.dumps(json.loads(l), ensure_ascii=False)))
        log("XLSX-CELL", "largest structure_json cell", big, "chars; Excel limit 32767;",
            "OK" if big <= 32767 else "OVER THE LIMIT")
        open(os.path.join(H, "UPLOAD_CELLCHECK.txt"), "w", encoding="utf-8").write(
            "largest structure_json cell: %d chars (Excel limit 32,767) -> %s\n"
            % (big, "within the limit" if big <= 32767 else "OVER THE LIMIT"))
    except Exception as e:
        log("CELLCHECK-FAILED", type(e).__name__, str(e)[:200])
    note_stage("upload"); git(None, "Phase 2F Part 1: annotations_cz_final.jsonl + upload_cz_final.xlsx")

    pres, cum = rows_present(), spend()
    if stops or over:
        finish("STOPPED EARLY: %s; %d rows assembled, %d headless tokens" % (stops or "tripwire", pres, cum),
               "# PART 1 stopped early\n\nStop files: %s\nOver tripwire: %s\nTokens: %d\nRows present: %d\n\n"
               "Everything complete was assembled and the upload package was built over it; nothing was "
               "uploaded and nothing was written to the database.\n" % (stops, over, cum, pres))
    finish("OK: %d of %d rows, %d headless tokens, %.1f h" % (pres, TARGET_ROWS, cum, (time.time() - t0) / 3600.0))

if __name__ == "__main__":
    main()
