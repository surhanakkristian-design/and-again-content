import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
chef = [(0.28,0.39,0.17,0.25),(0.29,0.39,0.17,0.25),(0.28,0.39,0.17,0.25),(0.29,0.39,0.17,0.25),(0.26,0.39,0.19,0.25),(0.26,0.38,0.19,0.26),(0.24,0.38,0.20,0.27),(0.27,0.38,0.20,0.27)]
man = [(0.53,0.38,0.22,0.42),(0.53,0.38,0.25,0.42),(0.53,0.38,0.22,0.42),(0.53,0.38,0.25,0.42),(0.53,0.36,0.25,0.44),(0.53,0.36,0.25,0.44),(0.55,0.35,0.25,0.46),(0.57,0.35,0.25,0.46)]
cha = [(0.28,0,0.46,0.34)]*8
write({"mediaId":5635,"level":"B","keyWord":"be under pressure","defaultVoice":"female","taps":[
 {"phrase":"to place a sugar shard","target":"the chef","voice":"female","keys":K(T8,chef)},
 {"phrase":"to fold his arms","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to hang from the painted ceiling","target":"the chandelier","voice":"female","keys":K(T8,cha)}],
 "stillS":0.2,
 "nouns":[{"word":"a chandelier","x":0.50,"y":0.20,"voice":"female"},{"word":"a cake","x":0.49,"y":0.50,"voice":"female"},{"word":"a tablecloth","x":0.45,"y":0.70,"voice":"female"},{"word":"a parquet floor","x":0.50,"y":0.88,"voice":"female"}],
 "question":"What is the chef doing?",
 "answer":["She","is","placing","a","sugar","shard","on","the","cake."],
 "answerVoice":"female",
 "notes":"Four people stand close together; only the chef and the man in the navy suit are targets. The chef's lower body is hidden by the cake and the table, so her box covers head, torso and hands and overlaps the cake (not a target). The man's box overlaps the woman in green (not a target). The shard she adds is small; her hands at the cake are clear. Key phrase 'be under pressure' is abstract and not placed as a noun."})
