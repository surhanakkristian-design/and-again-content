import json,re
MARK=re.compile(r"\[[^\]]*\]|\([^\)]*\)|\*[^\*]{1,60}\*|♪+")
def sentences(t):
    if not t: return []
    s=MARK.sub(" ",t)
    s=re.sub(r"(^|\s)[-–—]\s+"," ",s)          # dialogue dashes
    s=re.sub(r"\s+"," ",s).strip()
    if not s: return []
    parts=re.split(r"(?<=[.!?…])[\"”']?\s+(?=[\"“']?[A-Za-z0-9¿¡])",s)
    out=[]
    for p in parts:
        p=p.strip().strip("-–— ").strip()
        if not re.search(r"[A-Za-z]",p): continue
        out.append(p)
    return out
SUBJ=r"(?:i|you|he|she|it|we|they|this|that|there|these|those|everyone|everybody|someone|nobody|nothing|something|everything|who|my \w+|your \w+|his \w+|her \w+|our \w+|their \w+|the \w+|mom|dad)"
VERB_AFTER=r"(?:'m|'re|'s|'ve|'ll|'d|’m|’re|’s|’ve|’ll|’d|\s+(?:am|are|is|was|were|have|has|had|do|does|did|don't|doesn't|didn't|can|can't|could|couldn't|will|won't|would|should|must|may|might|need|needs|want|wants|love|loves|like|likes|see|sees|know|knows|think|thinks|got|get|gets|go|goes|went|made|make|makes|look|looks|feel|feels|found|bet|hate|hates|hear|miss|say|said|told|win|won|did|just \w+|really \w+|never \w+|always \w+|finally \w+|still \w+|also \w+|all \w+))\b"
FULL=re.compile(r"(?:^|[\s,])"+SUBJ+VERB_AFTER,re.I)
INV=re.compile(r"^(?:is|are|was|were|do|does|did|can|could|will|would|should|have|has|am)\s+(?:i|you|he|she|it|we|they|this|that|there|the|my|your)\b",re.I)
def det(sents):
    if not sents: return False,"no speech"
    if any(FULL.search(x) or INV.search(x) for x in sents): return True,"subject+verb pattern"
    toks=[re.findall(r"[A-Za-z']+",x) for x in sents]
    PRON={"i","you","he","she","it","we","they","this","that","there","these","those","i'm","you're","it's","that's","we're","they're","he's","she's","there's","i've","you've","we've"}
    if all(len(t)<=2 for t in toks) and not any(w.lower() in PRON for t in toks for w in t):
        return False,"only short fragments (<=2 words each, no subject pronoun)"
    return None,"unclear"
if __name__=="__main__":
    m=json.load(open("media_text_map.json")); res={}
    import collections; c=collections.Counter()
    for k,v in m.items():
        ss=sentences(v["transcript"]); d,why=det(ss) if v["transcript"] else (None,"no transcript")
        res[k]={"title":v["title"],"transcript":v["transcript"],"speech_sentences":ss,"det":d,"det_reason":why}
        c[(d,why)]+=1
    json.dump(res,open("split_det.json","w"),ensure_ascii=False,indent=0)
    for k,n in c.items(): print(n,k)
