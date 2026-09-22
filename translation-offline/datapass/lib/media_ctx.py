"""Parse MEDIA blocks of the 6.9.2026 translation SOURCE files (Drive) into E id -> media context."""
import glob, json, os, re
BASE = os.path.expanduser("~/Meine Ablage/And Again/Excels/Claude/6.9.2026-part1-translations")
pats = ["partsA/work/part2/lang/run_*/SOURCE*.txt", "partsA/work/part3/lang/run_*/SOURCE*.txt",
        "partsB/work/B*/lang/run_*/SOURCE*.txt"]
media, e2m, e2info = {}, {}, {}
for p in pats:
    for f in sorted(glob.glob(os.path.join(BASE, p))):
        cur = None
        for line in open(f, encoding="utf-8"):
            line = line.rstrip("\n")
            m = re.match(r"MEDIA (\d+) \| concept (\d+) \| (\w+)", line)
            if m:
                cur = int(m.group(1)); media.setdefault(cur, {"concept": int(m.group(2)), "kind": m.group(3)})
                continue
            if cur is None:
                continue
            for key, lab in [("word", "All Words word (as displayed): "), ("meaning", "meaning of the word: "),
                             ("irony", "irony: "), ("scene", "explanation of the video: ")]:
                if line.startswith(lab):
                    media[cur][key] = line[len(lab):]
            m = re.match(r"E (\d+) \| type (\d+) ([^|]+)\| style (\S+) \| exception: ([^|]+)\| options (\d)", line)
            if m:
                e = int(m.group(1)); e2m[e] = cur
                e2info[e] = {"style": m.group(4), "exception": m.group(5).strip(), "options": int(m.group(6))}
json.dump({"media": media, "e2m": e2m, "e2info": e2info},
          open(os.path.join(os.path.dirname(__file__), "..", "snapshot", "media_ctx.json"), "w"), ensure_ascii=False)
print(len(media), len(e2m))
