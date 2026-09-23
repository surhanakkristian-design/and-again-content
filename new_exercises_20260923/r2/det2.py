"""Deterministic first path for eligibility v2 (finite verb). Clear yes / clear no, the rest -> judge."""
import json,re,sys
sys.path.insert(0,"..")
from split import FULL,INV
IMP=r"(?:look|take|come|give|hold|let's|let|lets|stop|wait|put|get|go|try|open|close|watch|listen|help|keep|make|pass|push|pull|pour|grab|throw|catch|sit|stand|move|bring|show|tell|say|pick|hand|eat|drink|taste|smell|feel|touch|run|jump|follow|leave|turn|press|cut|shake|mix|add|use|wear|put|read|write|draw|call|ask|tell|share|save|hurry|relax|breathe|smile|dance|sing|clean|fix|kick|throw|check|see|hear|trust|remember|forget|meet|hit|drop|lift|carry|fill|slide|spin|flip|pay|buy|sell|find|lock|unlock|climb|swim|fly|ride|drive|park|sleep|wake|dream|cook|bake|boil|serve|enjoy|welcome|thank|bless|don't|do|be|stay|calm|shut|hide|duck|mind|excuse|pardon|forgive|guess|imagine|believe|trust|welcome)"
IMP_RE=re.compile(r"^(?:(?:oh|ok|okay|hey|now|so|yes|no|please|and|come on|alright|all right|well|here|quick|quickly|guys|babe|honey|dude|wow),?\s+)*"+IMP+r"\b(?:\s+(?:it|me|this|that|the|a|an|at|on|up|out|down|here|there|your|my|him|her|them|us|off|in|over|away|back|some|all|to|with|for|like|now|please|you|one|these|those|inside|outside|around|closer|together|slowly|carefully|fast|quick|quickly))",re.I)
CONTR=re.compile(r"\b\w+(?:'|’)(?:s|re|m|ve|ll|d)\b|n't\b|n’t\b",re.I)
NOVERB=set("""oh ah aah ahh wow whoa woah yes yeah yep yup no nope nah okay ok oops ouch ow hey hi hello bye goodbye ta-da tada yay hooray hmm hm uh um huh ha haha hahaha aw aww awesome cool nice great perfect amazing beautiful delicious yum yummy so good very too wow! ugh eww ew phew whew gosh god my oh-oh uh-oh wait? boom bam wham pow woo woohoo whoo whoa-oh ooh oooh omg jeez geez yikes voila voilà ready bravo cheers hurray huzzah hm-hmm mm mmm mmmm hmmm oof ooh-la-la la ooh-ooh aha a-ha ahem shh shhh psst the a an and or but of in on at to for with my your our their his her its this that these those one two three four five six seven eight nine ten again more please thanks sorry excellent fantastic incredible wonderful gorgeous lovely cute sweet fun funny crazy wild insane huge tiny big small hot cold warm fresh new old best better worst bad right wrong true exactly definitely absolutely totally really super mega ultra almost finally now here there not no-no oh-no oh-my yes! yes-yes""".split())
def det2(sents):
    if not sents: return False,"no speech"
    if any(FULL.search(x) or INV.search(x) for x in sents): return True,"subject+finite verb pattern"
    if any(IMP_RE.search(x.strip(" \"'“”")) for x in sents): return True,"imperative pattern"
    if any(CONTR.search(x) for x in sents): return None,"unclear (contraction)"
    toks=[w.lower().strip("'’-") for x in sents for w in re.findall(r"[A-Za-z'’\-]+|\d+",x)]
    toks=[t for t in toks if t]
    if toks and all(t in NOVERB or t.isdigit() for t in toks): return False,"only interjections/non-verb words"
    return None,"unclear"
if __name__=="__main__":
    S=json.load(open("../split_det.json")); res={}; import collections; c=collections.Counter()
    for k,v in S.items():
        ss=v["speech_sentences"]
        if not ss: continue
        d,why=det2(ss); res[k]={"title":v["title"],"speech_sentences":ss,"det":d,"det_reason":why}; c[(d,why)]+=1
    json.dump(res,open("det2.json","w"),ensure_ascii=False,indent=0)
    print(len(res)); [print(n,k) for k,n in c.most_common()]
