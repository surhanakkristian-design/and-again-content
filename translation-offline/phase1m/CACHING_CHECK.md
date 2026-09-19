# Phase 1M — caching check on `loader_1k.load_fresh_annotations` (brief §4)

The loader body (`phase1k/loader_1k.py` lines 196-199), verbatim:

```python
def load_fresh_annotations(purpose='', path=None):
    a = json.load(open(path or os.path.join(FRESH, 'annotations_fresh.json'), encoding='utf-8'))
    _log('1k:fresh', 'annotations', len(a), purpose)
    return a
```

There is no module-level memo (contrast `loader_1k._rewrites`, which *does* cache into the
global `_RW` and returns `dict(_RW)`). Every call re-opens the file and re-parses the JSON.

## Runtime result (two consecutive calls in one process)

* top-level dicts are the same object: **False**
* per-sid nested objects are the same object (sid `140001`): **False**

**Verdict: fresh-object-per-call.** A mutation of the returned annotations (e.g. `apply_hygiene`, which rewrites
`hy['v']` in place) therefore affects ONLY the copy held by the caller; the next loader call
returns pristine annotations. Conversely, a caller that wants the hygienised annotations to
persist across calls must keep its own reference.
