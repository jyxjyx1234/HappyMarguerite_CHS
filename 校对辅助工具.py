import re
import json

yiwen=open('.\译文\Marguerite_strings.json','r',encoding='utf8')
yiwenout=open('.\译文\Marguerite_strings1.json','w',encoding='utf8')
out=[]
yiwen=json.load(yiwen)

for dic in yiwen:
    if ('ちーちゃん' in dic["pre_jp"]) or ('ちーちゃ' in dic["pre_jp"]):
        if '小千' not in dic['post_zh_preview']:
            if '小～千' not in dic['post_zh_preview']:
                print(dic["index"])
            
