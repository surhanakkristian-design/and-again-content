import json
p='content/4885.json'; c=json.load(open(p))
c['question']="What is the woman doing?"
c['answer']=["She","is","walking","along","the","street."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
