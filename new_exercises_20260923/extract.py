import openpyxl, glob, os, json, re, collections
roots=[os.path.expanduser(p) for p in ["~/Documents/Claude","~/Meine Ablage/And Again/Excels"]]
files=[]
for r in roots:
    for f in glob.glob(r+"/**/*.xlsx",recursive=True):
        if "/~$" in f or "/logs/" in f: continue
        files.append(f)
recs=collections.defaultdict(list)  # id -> list of (mtime,file,word,vo,expl)
used=[]
for f in sorted(set(files)):
    wb=openpyxl.load_workbook(f,read_only=True)
    if "All Words" not in wb.sheetnames: wb.close(); continue
    ws=wb["All Words"]; it=ws.iter_rows(values_only=True)
    h=[str(c).strip() if c is not None else "" for c in next(it)]
    if "media_id" not in h or "Voiceover" not in h: wb.close(); continue
    ci={k:h.index(k) for k in ["media_id","word","Voiceover"]}
    li=h.index("Level (A/B)") if "Level (A/B)" in h else None
    ei=h.index("Explanation of the video") if "Explanation of the video" in h else None
    mt=os.path.getmtime(f); n=0
    for row in it:
        if row is None or len(row)<=ci["media_id"]: continue
        mid=row[ci["media_id"]]
        try: mid=int(float(mid))
        except: continue
        g=lambda i: (str(row[i]).strip() if i is not None and i<len(row) and row[i] is not None else "")
        recs[mid].append(dict(mtime=mt,file=f.replace(os.path.expanduser("~")+"/",""),word=g(ci["word"]),vo=g(ci["Voiceover"]),expl=g(ei),level=g(li)))
        n+=1
    used.append((f.replace(os.path.expanduser("~")+"/",""),n,mt)); wb.close()
json.dump({"files":used,"recs":recs},open("raw_records.json","w"))
print(len(used),"files",len(recs),"ids")
for u in used: print(u[1],u[0])
