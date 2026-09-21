#!/usr/bin/env python3
"""Phase 2H tests.  Imports run_2h and drives its REAL code paths; ONLY the model call (run_2h.spawn_claude, the
subprocess spawn of `claude`) is mocked.  Every test runs in its own temp dir; phase2h/out and every input stay
untouched (inputs are only read).  Prints PASS/FAIL per test + a SUMMARY line; exit 0 only if all pass."""
import os, sys
sys.dont_write_bytecode = True
import json, glob, random, shutil, tempfile, traceback, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run_2h as R

R.QUIET = True
R.SLEEP = lambda s: None
R.load_token = lambda: None            # never touch the real token in tests
G2 = R.G2
F2S = os.path.join(R.F2, "out", "sessions")
TMPS, RESULTS = [], []

class Mock:
    def __init__(self, fn): self.calls, self.fn = 0, fn
    def __call__(self, prompt, timeout):
        self.calls += 1
        return self.fn(prompt, self.calls)

def _no_call(p, c): raise AssertionError("model called although it must not be")
USAGE = {"input_tokens": 10, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 100}
def env_ok(rows):
    return 0, json.dumps({"type": "result", "subtype": "success", "is_error": False, "num_turns": 1, "usage": USAGE,
                          "result": json.dumps(rows, ensure_ascii=False)}, ensure_ascii=False), ""

# real stored model outputs (phase2f, read only): v / rw / lk of chunk cz_0001_s01 (n 4065-4164)
STORE = {k: {o["n"]: o for o in json.load(open(os.path.join(F2S, "cz_0001_s01_%s.json" % k), encoding="utf-8"))["rows"]}
         for k in ("v", "rw", "lk")}
def prompt_ns(p):
    ns = []
    for l in p.splitlines():
        l = l.strip()
        if l.startswith("{"):
            try: o = json.loads(l)
            except Exception: continue
            if isinstance(o, dict) and isinstance(o.get("n"), int): ns.append(o["n"])
    return ns
def kind_of(p): return "lk" if p.startswith(R.LK_2D) else ("rw" if p.startswith(R.REWRITE) else "v")
def store_mock():
    return Mock(lambda p, c: env_ok([STORE[kind_of(p)][n] for n in prompt_ns(p) if n in STORE[kind_of(p)]]))

def fresh():
    td = tempfile.mkdtemp(prefix="test_2h_")
    TMPS.append(td)
    R.BATCH_DEFS_OVERRIDE = None; R.LK_TARGETS_OVERRIDE = None; R.GATE_COUNTS_HOOK = None
    R.spawn_claude = Mock(_no_call)
    R.configure(td, commit=False, dry=False)
    R.CAP = 10 ** 9
    return td

def check(name, fn):
    try:
        d = fn()
        print("PASS", name, "-", d or "")
        RESULTS.append(True)
    except Exception as e:
        print("FAIL", name, "-", "%s: %s" % (type(e).__name__, str(e)[:1800]))
        for l in traceback.format_exc().splitlines()[-6:]:
            print("   ", l)
        RESULTS.append(False)

def jl(p): return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
STOPC = lambda: {"agv4": collections.Counter(ERROR=30, AGREE=15), "reader_nom": collections.Counter(AGREE=45), "g4_diag": collections.Counter()}

# ------------------------------------------------------------------------------------------------ T1
def t1():
    tlp = [json.loads(l) for l in open(os.path.join(G2, "session_timeline.jsonl"), encoding="utf-8") if l.strip()]
    # 2G never stored p07's full stdout: only the redacted last 400 characters of each successful output survive
    # (session_timeline.jsonl "text"; REFUSED_PIECES.md quotes the same text).  That stored fragment is embedded
    # VERBATIM as the tail of the envelope below (asserted), the rows before it are rebuilt for n 5425-5434.
    frag = next(e["text"] for e in tlp if e.get("session") == "cz_0002_s04_v_p07" and e.get("event") == "http_error")
    info = []
    for base in (5425, 6425, 7425):
        td = fresh()
        rows = [R.BYN[n] for n in range(base, base + 10)]
        mrows = [{"n": r["n"], "v": [r["en"]], "lk": [r.get("correct_answer_en") or ""], "lk_verdict": "exact",
                  "lk_reason": "fixture", "voice": "active_prodrop", "subject": None, "agent_nom": False,
                  "embedded_agents": [], "gender": "m", "tf": "present", "tense_open": False, "fragment": False,
                  "main_sentence_index": 0, "person": "3sg", "number": "sg"} for r in rows]
        env = {"is_error": False, "num_turns": 1, "usage": USAGE,
               "result": json.dumps(mrows, ensure_ascii=False, separators=(",", ":")),
               "ttft_ms": 13308, "type": "result", "duration_ms": 24353, "uuid": "d72fa92f-10af-4133-99ce-9893349dd785",
               "ttft_stream_ms": 803, "time_to_request_ms": 26, "first_content_frame_ms": 803, "queued_turn_count": 0,
               "result_index": 0}
        stdout = json.dumps(env, ensure_ascii=False, separators=(",", ":"))
        assert str(base + 4) in stdout, "fixture lacks n=%d" % (base + 4)
        if base == 5425:
            assert stdout.endswith(frag), "stored p07 fragment not reproduced verbatim"
        m = Mock(lambda p, c: (0, stdout, "HTTP/1.1 200 (stderr noise with 429 in it)"))
        R.spawn_claude = m
        path = os.path.join(td, "s.json")
        st, got = R.run_session("t1_%d_v" % base, "v", "PROMPT", rows, 1000, path, "annotate")
        meta = json.load(open(path, encoding="utf-8"))["meta"]
        assert st == "OK" and len(got) == 10, (st, got if isinstance(got, str) else len(got))
        assert m.calls == 1, "retried: %d calls" % m.calls
        assert meta["envelope"] == "success" and meta["exit"] == 0 and meta["attempts"] == 1
        info.append("n=%d: 1 call, SUCCESS" % (base + 4))
    return "; ".join(info) + " (fixture tail = stored p07 fragment, %d chars)" % len(frag)

# ------------------------------------------------------------------------------------------------ T2
def t2():
    C = R.classify
    assert C(0, json.dumps({"type": "result", "is_error": False, "result": "429 Too Many Requests n=5429"}), "HTTP 429")["kind"] == "success"
    assert C(0, json.dumps({"type": "result", "is_error": False, "result": "usage limit quota 429"}), "")["kind"] == "success"
    assert C(0, json.dumps({"type": "assistant", "text": "429"}), "429")["retry"] is False
    k = C(1, json.dumps({"type": "result", "is_error": True, "api_error_status": 429, "result": "API Error: 429"}), "")
    assert k["kind"] == "rate_limit" and k["retry"], k
    k = C(0, json.dumps({"type": "result", "is_error": True, "error": {"type": "error", "error": {"type": "rate_limit_error", "message": "per-minute rate"}}}), "")
    assert k["kind"] == "rate_limit" and k["retry"], k
    assert C(0, json.dumps({"type": "result", "is_error": True, "error": {"type": "overloaded_error"}}), "")["kind"] == "rate_limit"
    assert C(1, json.dumps({"type": "result", "is_error": True, "http_status": "429"}), "")["kind"] == "rate_limit"
    assert C(1, "", "some text 429")["kind"] == "exit_nonzero"          # retried because of the EXIT CODE, not the text
    td = fresh()
    seq = [(1, json.dumps({"type": "result", "is_error": True, "api_error_status": 429, "result": "API Error: 429 rate_limit_error"}), ""),
           env_ok([{"n": 4065}])]
    m = Mock(lambda p, c: seq[c - 1]); R.spawn_claude = m
    st, _ = R.run_session("t2_v", "v", "P", [R.BYN[4065]], 100, os.path.join(td, "a.json"), "annotate")
    assert st == "OK" and m.calls == 2, (st, m.calls)
    m2 = Mock(lambda p, c: (0, env_ok([{"n": 4066, "x": "429"}])[1], "429 429"))
    R.spawn_claude = m2
    st, _ = R.run_session("t2b_v", "v", "P", [R.BYN[4066]], 100, os.path.join(td, "b.json"), "annotate")
    assert st == "OK" and m2.calls == 1
    return "real 429 envelope retried (2 calls); 429 only in text/stderr -> 1 call"

# ------------------------------------------------------------------------------------------------ T3
def t3():
    rnd = random.Random(7)
    a = R._samp(rnd, [1, 2, 3], 250)
    b = R._samp(rnd, list(range(100)), 50)
    assert sorted(a) == [1, 2, 3] and len(b) == 50 and len(set(b)) == 50
    return "k=250 over 3 -> 3 items; k=50 over 100 -> 50"

# ------------------------------------------------------------------------------------------------ T4
def t4():
    g = R.gate_decide(7, 33)
    assert g["decision"] == "FLAG", g
    assert abs(g["cp95_pct"][0] - 8.98) <= 0.01 and abs(g["cp95_pct"][1] - 38.91) <= 0.01, g["cp95_pct"]
    g2 = R.gate_decide(7, 45)
    assert g2["decision"] == "FLAG" and g2["cp95_pct"][0] < 12.0 and g2["point_pct"] > 12.0, g2
    td = fresh()
    R.GATE_COUNTS_HOOK = lambda bid, pick: {"agv4": collections.Counter(ERROR=7, AGREE=26), "reader_nom": collections.Counter(AGREE=40),
                                            "g4_diag": collections.Counter()}
    gb = R.gate_batch("annotate", "cz_t4", [{"n": i} for i in range(60)])
    assert gb["decision"] == "FLAG" and os.path.exists(os.path.join(td, "FLAG_gate3_agv4_cz_t4.md"))
    assert not glob.glob(os.path.join(td, "STOP_*")), glob.glob(os.path.join(td, "STOP_*"))
    return "7/33 CP %s -> FLAG file, no STOP; 7/45 CP %s -> FLAG" % (g["cp95_pct"], g2["cp95_pct"])

def t4b():
    g = R.gate_decide(30, 35)
    assert g["decision"] == "FLAG" and g["cp95_pct"][0] > 12.0, g
    g0 = R.gate_decide(0, 0)
    assert g0["decision"] == "FLAG"
    g3 = R.gate_decide(30, 45)
    assert g3["decision"] == "STOP", g3
    return "30/35 (CP lower %.2f) -> FLAG only; 30/45 -> STOP" % g["cp95_pct"][0]

# ------------------------------------------------------------------------------------------------ T5
def t5():
    td = fresh()
    R.BATCH_DEFS_OVERRIDE = [("cz_t5a", list(range(4065, 4070))), ("cz_t5b", list(range(4070, 4075)))]
    R.GATE_COUNTS_HOOK = lambda bid, pick: STOPC() if bid == "cz_t5a" else R.gate_counts(pick)
    m = store_mock(); R.spawn_claude = m
    R.annotate(cap=10 ** 9)
    assert os.path.exists(os.path.join(td, "STOP_gate3_agv4_cz_t5a.md"))
    assert not glob.glob(os.path.join(td, "STOP_gate3_*_cz_t5b.md"))
    b = jl(os.path.join(td, "out", "annotations_cz_t5b.jsonl"))
    a = jl(os.path.join(td, "out", "annotations_cz_t5a.jsonl"))
    assert len(a) == 5 and all(x.get("gate3") == "STOP" for x in a) and len(b) == 5
    gates = json.load(open(os.path.join(td, "gates_2h.json")))["annotate"]
    assert gates["cz_t5a"]["decision"] == "STOP" and gates["cz_t5b"]["decision"] != "STOP"
    R.merge(); R.upload()
    import openpyxl
    ws = openpyxl.load_workbook(os.path.join(td, "out", "upload_cz_final.xlsx"), read_only=True)["cz"]
    ns = {json.loads(r[5])["n"] for r in ws.iter_rows(min_row=2, values_only=True)}
    assert not (ns & set(range(4065, 4070))) and set(range(4070, 4075)) <= ns
    fin = {x["n"]: x for x in jl(os.path.join(td, "out", "annotations_cz_final.jsonl"))}
    assert fin[4065].get("gate3") == "STOP" and fin[4070].get("gate3") is None
    return "cz_t5a STOP (rows written, marked, excluded from xlsx); cz_t5b %s, in xlsx; %d model calls" % (gates["cz_t5b"]["decision"], m.calls)

# ------------------------------------------------------------------------------------------------ T6
def t6():
    td = fresh()
    R.GATE_COUNTS_HOOK = lambda bid, pick: STOPC()
    m = Mock(_no_call); R.spawn_claude = m
    R.annotate(cap=10 ** 9, no_spawn=True, only=["cz_0004"])
    a = jl(os.path.join(td, "out", "annotations_cz_0004.jsonl"))
    assert os.path.exists(os.path.join(td, "STOP_gate3_agv4_cz_0004.md"))
    assert len(a) == 700, "%d rows written: %s" % (len(a), R.nranges([x["n"] for x in a]))
    assert all(x.get("gate3") == "STOP" for x in a) and m.calls == 0
    return "700 adopted cz_0004 rows written before the (forced) STOP: %s" % R.nranges([x["n"] for x in a])

# ------------------------------------------------------------------------------------------------ T7
def t7():
    td = fresh()
    for f in ("STOP_gate3_agv4_cz_0004.md", "FLAG_gate3_reader_nom_cz_gap.md", "STOP_rows_missing.md"):
        open(os.path.join(td, f), "w").write("x")
    R.LK_TARGETS_OVERRIDE = list(range(4065, 4075))
    m = store_mock(); R.spawn_claude = m
    R.lk_stage(cap=10 ** 9)
    assert m.calls >= 1, "lk blocked by an annotate stop file"
    td2 = fresh()
    open(os.path.join(td2, "STOP_gate3_agv4_lk.md"), "w").write("x")
    R.BATCH_DEFS_OVERRIDE = [("cz_t7", list(range(4065, 4070)))]
    m2 = store_mock(); R.spawn_claude = m2
    R.annotate(cap=10 ** 9)
    assert m2.calls >= 1, "annotate blocked by an lk stop file"
    td3 = fresh()
    open(os.path.join(td3, "STOP_token_cap.md"), "w").write("x")
    R.LK_TARGETS_OVERRIDE = list(range(4065, 4075))
    m3 = store_mock(); R.spawn_claude = m3
    R.lk_stage(cap=10 ** 9)
    assert m3.calls == 0
    return "gate STOP/FLAG files never block the other stage (lk %d calls, annotate %d calls); STOP_token_cap blocks (0 calls)" % (m.calls, m2.calls)

# ------------------------------------------------------------------------------------------------ T9 + T8
T9DIR = {}
def t9():
    td = fresh(); T9DIR["td"] = td
    ns = list(range(4065, 4075))
    R.BATCH_DEFS_OVERRIDE = [("cz_t9", ns)]; R.LK_TARGETS_OVERRIDE = ns
    m = store_mock(); R.spawn_claude = m
    R.annotate(cap=10 ** 9)
    ann = jl(os.path.join(td, "out", "annotations_cz_t9.jsonl"))
    assert len(ann) == 10, len(ann)
    R.lk_stage(cap=10 ** 9)
    lk = json.load(open(os.path.join(td, "lk_sessions_2h.json")))
    assert lk["rows_judged"] == 10, lk["rows_judged"]
    rep = R.merge(); up = R.upload()
    fin = jl(os.path.join(td, "out", "annotations_cz_final.jsonl"))
    assert len({x["n"] for x in fin}) == len(fin) and [x["n"] for x in fin] == sorted(x["n"] for x in fin)
    import openpyxl
    ws = openpyxl.load_workbook(os.path.join(td, "out", "upload_cz_final.xlsx"), read_only=True)["cz"]
    hdr = next(ws.iter_rows(min_row=1, max_row=1, values_only=True))
    assert list(hdr) == R.COLS, hdr
    nrow = sum(1 for _ in ws.iter_rows(min_row=2, values_only=True))
    assert nrow == up["rows"] == len(fin)
    rd = open(os.path.join(td, "UPLOAD_README.md"), encoding="utf-8").readline()
    assert "Phase 2H" in rd and "Phase 2D" not in rd, rd
    for f in ("gates_2h.json", "ledger_2h.json", "merge_2h.json", "PLAN_annotate.json", "PLAN_lk.json"):
        json.load(open(os.path.join(td, f)))
    jl(os.path.join(td, "session_timeline_2h.jsonl")); jl(os.path.join(td, "progress.log"))
    T9DIR["calls"] = m.calls
    return "10 rows: %d model calls; final %d rows (%s); xlsx %d rows; lk status %s" % (
        m.calls, len(fin), rep["sources"], nrow, [s["status"] for s in lk["sessions"].values()])

def t8():
    td = T9DIR["td"]
    R.configure(td, commit=False, dry=False); R.CAP = 10 ** 9
    ns = list(range(4065, 4075))
    R.BATCH_DEFS_OVERRIDE = [("cz_t9", ns)]; R.LK_TARGETS_OVERRIDE = ns
    m = Mock(_no_call); R.spawn_claude = m
    plan = R.annotate(cap=10 ** 9)
    R.lk_stage(cap=10 ** 9)
    assert m.calls == 0 and plan["sessions_to_run"] == 0, (m.calls, plan["sessions_to_run"])
    return "second invocation: 0 sessions planned, 0 spawns (first run made %d)" % T9DIR["calls"]

# ------------------------------------------------------------------------------------------------ T10 / T11
def t10():
    lkfinal = {a["n"]: a for a in jl(os.path.join(G2, "lk", "annotations_cz_final.jsonl"))}
    pre = {}
    for i in (2, 3):
        for a in jl(os.path.join(G2, "out", "annotations_cz_%04d.jsonl" % i)):
            pre[a["n"]] = a
    checked, bad, first = 0, 0, None
    for fp in sorted(glob.glob(os.path.join(G2, "lk", "sessions", "*_lk.json"))):
        for o in json.load(open(fp, encoding="utf-8")).get("rows") or []:
            n = o.get("n")
            if n in lkfinal and n in pre:
                checked += 1
                got = R.apply_lk(pre[n], o)
                if got != lkfinal[n]:
                    bad += 1
                    if first is None:
                        first = {"n": n, "lk_out": o, "diff": {k: [got.get(k), lkfinal[n].get(k)] for k in set(got) | set(lkfinal[n]) if got.get(k) != lkfinal[n].get(k)}}
    assert checked and not bad, "%d of %d rows differ from 2G's lk merge; first: %s" % (bad, checked, json.dumps(first, ensure_ascii=False)[:1500])
    return "apply_lk reproduces 2G's lk-merged rows on all %d rows 2G judged" % checked

def t11():
    k = 0
    for fp in sorted(glob.glob(os.path.join(G2, "lk", "sessions", "*_lk.json"))):
        p = json.load(open(fp, encoding="utf-8"))["prompt"]
        assert p.startswith(R.LK_2D)
        rows = [R.lk_row(n) for n in prompt_ns(p[len(R.LK_2D):])]
        assert R.lk_prompt(rows) == p, os.path.basename(fp)
        k += 1
    assert k
    import hashlib
    assert hashlib.sha256(R.LK_2D.encode()).hexdigest()[:16] == "5fa910459c078539"
    return "lk prompt byte-identical to 2G's stored prompts (%d sessions), sha16 5fa910459c078539" % k

# ------------------------------------------------------------------------------------------------ T12-T14
def t12():
    td = fresh()
    m = Mock(lambda p, c: (1, "", "Error: Invalid API key / not logged in")); R.spawn_claude = m
    try:
        R.run_session("t12_v", "v", "P", [R.BYN[4065]], 100, os.path.join(td, "a.json"), "annotate")
        raise AssertionError("no HardStop")
    except R.HardStop as e:
        assert str(e) == "first_session_failed"
    assert os.path.exists(os.path.join(td, "STOP_first_session_failed.md")) and m.calls == 1 and R.STATE["spent"] == 0
    return "first session exit 1 -> STOP_first_session_failed.md, 1 call, 0 tokens"

def t13():
    td = fresh()
    R.run_session("warm_v", "v", "P", [R.BYN[4066]], 100, os.path.join(td, "w.json"), "annotate") if False else None
    R.STATE["launch"] = 5                                   # not the first session
    m = Mock(lambda p, c: (1, json.dumps({"type": "result", "is_error": True, "api_error_status": 429,
                                          "result": "Claude AI usage limit reached. Your limit will reset at 5pm"}), ""))
    R.spawn_claude = m
    try:
        R.run_session("t13_v", "v", "P", [R.BYN[4065]], 100, os.path.join(td, "a.json"), "annotate")
        raise AssertionError("no HardStop")
    except R.HardStop as e:
        assert str(e) == "usage_limit"
    assert os.path.exists(os.path.join(td, "STOP_usage_limit.md")) and m.calls == 1
    R.STATE["stop"] = None                                  # a new process: only the FILE remains
    R.LK_TARGETS_OVERRIDE = list(range(4065, 4075))
    R.lk_stage(cap=10 ** 9)
    assert m.calls == 1
    return "usage-limit envelope -> STOP_usage_limit.md, no retry, lk then spawns 0"

def t14():
    td = fresh()
    R.CAP = 1000
    m = Mock(_no_call); R.spawn_claude = m
    st, why = R.run_session("t14_v", "v", "P", [R.BYN[4065]], 5000, os.path.join(td, "a.json"), "annotate")
    assert st == "STOP" and why == "token_cap" and os.path.exists(os.path.join(td, "STOP_token_cap.md")) and m.calls == 0
    return "reservation 0 + 0 + 5000 > cap 1000 -> STOP_token_cap.md before spawning"

if __name__ == "__main__":
    for name, fn in [("T1 success with 429 in row numbers is not retried", t1),
                     ("T2 rate limit only from the envelope", t2),
                     ("T3 _samp no recursion", t3),
                     ("T4 GATE 3 7/33 and 7/45 FLAG, not STOP", t4),
                     ("T4b GATE 3 <40 decided only FLAGS", t4b),
                     ("T5 GATE 3 STOP stops only its batch", t5),
                     ("T6 700 adopted cz_0004 rows written before a failing gate", t6),
                     ("T7 stop-file scoping between stages", t7),
                     ("T9 end to end 10 real rows annotate->lk->merge->upload", t9),
                     ("T8 resume spawns 0 sessions", t8),
                     ("T10 apply_lk reproduces 2G lk merge", t10),
                     ("T11 lk prompt byte-identical to 2G", t11),
                     ("T12 first session failure stops at 0 cost", t12),
                     ("T13 usage limit stops everything", t13),
                     ("T14 token cap reservation", t14)]:
        check(name, fn)
    for t in TMPS:
        shutil.rmtree(t, ignore_errors=True)
    ok = sum(RESULTS)
    print("SUMMARY: %d/%d PASS%s" % (ok, len(RESULTS), "" if ok == len(RESULTS) else " - %d FAIL" % (len(RESULTS) - ok)))
    sys.exit(0 if ok == len(RESULTS) else 1)
