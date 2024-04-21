import MeCab
import json
import re
#找出多次出现的片假名词作词典

mecab_tagger = MeCab.Tagger("-Owakati")

with open('.\OriginFile\Marguerite_strings.json','r',encoding='utf8') as f:
    wenben=json.load(f)


dic={}
for dics in wenben:
    text=dics['message']
    words=mecab_tagger.parse(text).split()[:-1]
    for word in words:
        if word not in dic:
            dic[word]=1

res=[]

for i in dic:
    if re.search('[\u30A0-\u30FF]',i):
        if len(i)>1:
            res.append((dic[i],i))

res.sort(reverse=True)
with open('高频词.json','w',encoding='utf8') as f:
    json.dump(res,f, ensure_ascii=False, indent=4)

