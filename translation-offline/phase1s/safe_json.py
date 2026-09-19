#!/usr/bin/env python3
"""Phase 1S — crash-proof JSON writing and run markers.

Why this exists: the 1Q final run made all 1,157 model calls and then died inside
`json.dump` on a Python `set` (`$.rows[*].f9_readout.sk.verdict`), leaving a 6 KB
fragment and NO `FINAL_RUN_DONE` marker. The verdicts were safe on disk; the run
looked unfinished. This module removes that whole failure class:

  * `safe_dump`  — never raises on an exotic type, writes atomically (tmp+fsync+os.replace).
  * `safe_dumps` — same encoder, string form.
  * `write_done_marker` / `guarded_run` — a marker ALWAYS exists after the run,
    either DONE or CRASHED-with-traceback, and the verdict log is flushed first.

No model, network, DB or app code is touched here.
"""
import io, json, math, os, sys, tempfile, traceback, datetime

__all__ = ["json_default", "_sanitise_keys", "safe_dumps", "safe_dump", "write_done_marker",
           "guarded_run", "flush_log"]


# --------------------------------------------------------------------------- #
# encoder
# --------------------------------------------------------------------------- #
def json_default(o):
    """Last-resort encoder. MUST NOT raise: an unknown object becomes a tagged
    repr string so that a serialisation surprise can never destroy a finished run.
    Anything converted this way is visible in the output (prefix `<unserialisable`
    or a plain list/str), so it cannot silently pass as real data."""
    # sets -> sorted list (the exact 1Q crash); sorting may fail on mixed types
    if isinstance(o, (set, frozenset)):
        try:
            return sorted(o)
        except Exception:
            return sorted(o, key=repr)
    if isinstance(o, tuple):
        return list(o)
    if isinstance(o, (bytes, bytearray, memoryview)):
        b = bytes(o)
        try:
            return b.decode("utf-8")
        except Exception:
            return {"__bytes_b64__": __import__("base64").b64encode(b).decode("ascii")}
    if isinstance(o, (datetime.datetime, datetime.date, datetime.time)):
        return o.isoformat()
    if isinstance(o, complex):
        return [o.real, o.imag]
    if isinstance(o, range):
        return list(o)
    # pathlib.Path and anything os.PathLike
    if hasattr(o, "__fspath__"):
        try:
            return os.fspath(o)
        except Exception:
            pass
    # numpy-like: scalars expose .item(), arrays expose .tolist()
    for meth in ("tolist", "item"):
        f = getattr(o, meth, None)
        if callable(f):
            try:
                return f()
            except Exception:
                pass
    # dataclasses / plain objects with a __dict__
    d = getattr(o, "__dict__", None)
    if isinstance(d, dict) and d:
        try:
            return {"__type__": type(o).__name__,
                    "__fields__": {k: v for k, v in d.items() if not k.startswith("_")}}
        except Exception:
            pass
    if isinstance(o, (list, tuple)):
        return list(o)
    try:
        return "<unserialisable %s: %s>" % (type(o).__name__, repr(o)[:400])
    except Exception:
        return "<unserialisable %s: repr() failed>" % type(o).__name__


_SAFE_KEY = (str, int, float, bool, type(None))


def _sanitise_keys(o, _seen=None):
    """`json.dumps(default=...)` only ever sees VALUES: a dict key of an exotic
    type (tuple, set, object) raises `TypeError: keys must be str...` no matter what
    default is passed. So keys get their own pre-pass. Containers are rebuilt, leaves
    are left to `json_default`. Cycles become a marker string instead of RecursionError."""
    _seen = _seen or set()
    if isinstance(o, dict):
        if id(o) in _seen:
            return "<circular dict>"
        _seen = _seen | {id(o)}
        out = {}
        for k, v in o.items():
            if not isinstance(k, _SAFE_KEY):
                try:
                    k = "__key__" + repr(k)
                except Exception:
                    k = "__key__<unreprable %s>" % type(k).__name__
            elif isinstance(k, bool) or k is None or isinstance(k, (int, float)):
                pass
            out[k] = _sanitise_keys(v, _seen)
        return out
    if isinstance(o, (list, tuple)):
        if id(o) in _seen:
            return "<circular list>"
        return [_sanitise_keys(v, _seen | {id(o)}) for v in o]
    return o


def safe_dumps(obj, indent=1, sort_keys=False, allow_nan=True):
    """json.dumps that cannot raise TypeError on an exotic value.
    NaN/Infinity: kept as the JSON5-ish literals Python emits (allow_nan=True,
    the stdlib default) unless the caller asks for strict JSON, in which case
    they are rewritten to null by a second pass."""
    obj = _sanitise_keys(obj)
    if allow_nan:
        return json.dumps(obj, ensure_ascii=False, indent=indent,
                          sort_keys=sort_keys, default=json_default)
    cleaned = _denan(obj)
    return json.dumps(cleaned, ensure_ascii=False, indent=indent,
                      sort_keys=sort_keys, default=json_default, allow_nan=False)


def _denan(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {k: _denan(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_denan(v) for v in o]
    return o


def safe_dump(obj, path, indent=1, sort_keys=False, allow_nan=True):
    """Serialise FIRST (in memory), then write atomically.

    Order matters: if encoding somehow still failed, the previous file on disk is
    left untouched instead of being truncated to a fragment — the exact damage the
    1Q crash did. The write is tmp-file + flush + fsync + os.replace, so a reader
    (or a later run) sees either the old complete file or the new complete file,
    never a half one. Returns the path written."""
    path = os.fspath(path)
    text = safe_dumps(obj, indent=indent, sort_keys=sort_keys, allow_nan=allow_nan)
    d = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix="." + os.path.basename(path) + ".", suffix=".tmp")
    try:
        with io.open(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)           # atomic within the filesystem
        tmp = None
    finally:
        if tmp is not None and os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass
    try:                                 # make the rename itself durable
        dfd = os.open(d, os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    except OSError:
        pass
    return path


# --------------------------------------------------------------------------- #
# markers
# --------------------------------------------------------------------------- #
def flush_log(fh):
    """Flush + fsync a verdict/call log handle; never raises."""
    try:
        fh.flush()
        os.fsync(fh.fileno())
        return True
    except Exception:
        return False


def write_done_marker(path, meta=None, status="DONE", exc=None):
    """Write the run marker atomically. `status` is DONE or CRASHED.
    On CRASHED the traceback is embedded so the next session knows the calls were
    made and only the write failed."""
    rec = {"status": status,
           "written_utc": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
           "pid": os.getpid()}
    if meta:
        rec["meta"] = meta
    if exc is not None:
        rec["error"] = {"type": type(exc).__name__, "msg": str(exc)[:2000],
                        "traceback": "".join(traceback.format_exception(
                            type(exc), exc, exc.__traceback__))[-8000:]}
    safe_dump(rec, path, indent=1)
    return rec


def guarded_run(fn, done_path, meta_fn=None, logs=()):
    """Run `fn`; whatever happens, flush the logs and leave a marker.

    try/finally shape required by the brief: the calls are already paid for by the
    time `fn` returns, so the marker must not depend on the result write succeeding.
    """
    status, exc, result = "DONE", None, None
    try:
        result = fn()
    except BaseException as e:            # noqa: BLE001 - deliberate: marker first
        status, exc = "CRASHED", e
        raise
    finally:
        for fh in logs:
            flush_log(fh)
        meta = None
        try:
            meta = meta_fn(result) if meta_fn else None
        except Exception as me:
            meta = {"meta_fn_failed": repr(me)}
        try:
            write_done_marker(done_path, meta=meta, status=status, exc=exc)
        except Exception:
            # absolutely last resort: a bare marker with no JSON at all
            try:
                with open(os.fspath(done_path), "w", encoding="utf-8") as fh:
                    fh.write(status + "\n")
            except Exception:
                pass
    return result


# --------------------------------------------------------------------------- #
# self-test
# --------------------------------------------------------------------------- #
def _selftest(tmpdir=None):
    import pathlib, shutil
    tmpdir = tmpdir or tempfile.mkdtemp(prefix="safe_json_selftest_")
    ok, fails = 0, []

    def check(name, cond, extra=""):
        nonlocal ok
        if cond:
            ok += 1
            print("  PASS  %-42s %s" % (name, extra))
        else:
            fails.append(name)
            print("  FAIL  %-42s %s" % (name, extra))

    class Custom:
        def __init__(self):
            self.a, self.b, self._hidden = 1, {"x"}, "no"

    class Opaque:
        __slots__ = ()

    class FakeNumpyScalar:
        def item(self):
            return 42

    class FakeNumpyArray:
        def tolist(self):
            return [1, 2, 3]

    obj = {
        "sets": {"nested": {"future", "present"}, "frozen": frozenset([3, 1, 2])},
        "mixed_set": {1, "a", None},
        "tuple_value": (1, 2, ("deep", {"s"})),
        ("tuple", "key"): "tuple keys are coerced by json itself",
        "custom": Custom(),
        "cycle": None,
        "opaque": Opaque(),
        "numpy_scalar": FakeNumpyScalar(),
        "numpy_array": FakeNumpyArray(),
        "bytes": b"hello",
        "badbytes": b"\xff\xfe",
        "path": pathlib.Path("/tmp/x/y.json"),
        "when": datetime.datetime(2026, 9, 19, 12, 0, 0),
        "nan": float("nan"), "inf": float("inf"), "ninf": float("-inf"),
        "rows": [{"f9_readout": {"sk": {"verdict": {"future", "present"}}}}],
    }

    cyc = {"self": None}; cyc["self"] = cyc
    obj["cycle"] = cyc

    # 1. plain json.dump still fails on this (i.e. the test object is real)
    try:
        json.dumps(obj)
        base_raises = False
    except TypeError:
        base_raises = True
    check("stdlib json.dumps rejects the object", base_raises)

    # 2. safe_dumps does not raise, output parses
    s = safe_dumps(obj)
    back = json.loads(s)
    check("safe_dumps does not raise", True, "%d chars" % len(s))
    check("sets -> sorted lists", back["sets"]["nested"] == ["future", "present"]
          and back["sets"]["frozen"] == [1, 2, 3])
    check("mixed-type set survives (repr key)", isinstance(back["mixed_set"], list)
          and len(back["mixed_set"]) == 3)
    check("tuple -> list, nested set inside", back["tuple_value"][2] == ["deep", {"s": None}]
          or back["tuple_value"][2][1] == ["s"], str(back["tuple_value"]))
    check("tuple dict KEY is coerced, no raise",
          any(k.startswith("__key__") for k in back if isinstance(k, str)),
          [k for k in back if k.startswith("__key__")][0] if any(
              k.startswith("__key__") for k in back) else "none")
    check("custom class -> __type__/__fields__",
          back["custom"]["__type__"] == "Custom" and back["custom"]["__fields__"]["b"] == ["x"]
          and "_hidden" not in back["custom"]["__fields__"])
    check("opaque object -> repr string, no raise",
          isinstance(back["opaque"], str) and back["opaque"].startswith("<unserialisable Opaque"))
    check("numpy-like scalar/array", back["numpy_scalar"] == 42 and back["numpy_array"] == [1, 2, 3])
    check("bytes -> utf-8 / base64", back["bytes"] == "hello" and "__bytes_b64__" in back["badbytes"])
    check("Path -> str", back["path"] == "/tmp/x/y.json")
    check("datetime -> isoformat", back["when"].startswith("2026-09-19T12:00:00"))
    check("the exact 1Q crash site encodes",
          back["rows"][0]["f9_readout"]["sk"]["verdict"] == ["future", "present"])
    check("NaN/Inf kept by default", math.isnan(back["nan"]) and math.isinf(back["inf"]))
    check("cycle -> marker, no RecursionError",
          isinstance(back["cycle"]["self"], str) and "circular" in back["cycle"]["self"])
    check("sort_keys with mixed key types", isinstance(safe_dumps(obj, sort_keys=True), str))
    strict = json.loads(safe_dumps(obj, allow_nan=False))
    check("NaN/Inf -> null under allow_nan=False",
          strict["nan"] is None and strict["inf"] is None and strict["ninf"] is None)

    # 3. atomicity: the old file survives a failed encode, and replace is atomic
    p = os.path.join(tmpdir, "results.json")
    safe_dump({"first": True}, p)
    check("safe_dump writes", json.load(open(p)) == {"first": True})
    safe_dump(obj, p)
    check("safe_dump overwrites atomically", json.load(open(p))["path"] == "/tmp/x/y.json")
    check("no .tmp litter left",
          not [f for f in os.listdir(tmpdir) if f.endswith(".tmp")], str(os.listdir(tmpdir)))

    # 4. markers, happy path and crash path
    done = os.path.join(tmpdir, "FINAL_RUN_DONE")
    logf = open(os.path.join(tmpdir, "calls.jsonl"), "w", encoding="utf-8")
    logf.write('{"call": 1}\n')
    guarded_run(lambda: {"rows": 1080}, done, meta_fn=lambda r: {"rows": r["rows"]}, logs=[logf])
    m = json.load(open(done))
    check("DONE marker after a clean run", m["status"] == "DONE" and m["meta"]["rows"] == 1080)
    check("log flushed to disk", os.path.getsize(os.path.join(tmpdir, "calls.jsonl")) > 0)

    done2 = os.path.join(tmpdir, "FINAL_RUN_DONE_crash")

    def boom():
        json.dumps({"v": {1, 2}})     # the 1Q crash, verbatim
    try:
        guarded_run(boom, done2, logs=[logf])
    except TypeError:
        pass
    m2 = json.load(open(done2))
    check("CRASHED marker + traceback on failure",
          m2["status"] == "CRASHED" and m2["error"]["type"] == "TypeError"
          and "json" in m2["error"]["traceback"])
    logf.close()

    # 5. marker write itself uses the safe encoder
    done3 = os.path.join(tmpdir, "FINAL_RUN_DONE_meta")
    write_done_marker(done3, meta={"frames": {"past", "present"}, "obj": Opaque()})
    m3 = json.load(open(done3))
    check("marker meta with a set survives", m3["meta"]["frames"] == ["past", "present"])

    print("\nself-test: %d checks, %d failed %s" % (ok + len(fails), len(fails), fails or ""))
    shutil.rmtree(tmpdir, ignore_errors=True)
    return not fails


if __name__ == "__main__":
    sys.exit(0 if _selftest() else 1)
