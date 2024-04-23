import re
import json

yiwen=open('.\译文\Marguerite_strings.json','r',encoding='utf8')
yiwenout=open('.\译文\Marguerite_strings1.json','w',encoding='utf8')
out=[]
yiwen=json.load(yiwen)

for dic in yiwen:
    if 'さくら' in dic["pre_jp"]:
        if "咲良" not in dic["pre_jp"]:
            dic["post_zh_preview"]=dic["post_zh_preview"].replace('樱','さくら').replace('咲良','さくら').replace('咲','さ')
    
    if 'まお' in dic["pre_jp"]:
        if "真央" not in dic["pre_jp"]:
            dic["post_zh_preview"]=dic["post_zh_preview"].replace('真央','まお')
    out.append(dic)

json.dump(out,yiwenout,ensure_ascii=False,indent=4)
            
