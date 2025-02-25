#封包用
import codecs
import re
import json
from hanzidict import hanzidict

source_chars=''
target_chars=''

def teshuzifutihuan(text):#匹配时去除特殊字符
    text = text.replace("♪", "").replace("・", "").replace("〜", "").replace("～", "").replace("?", "").replace(" ", "").replace('\u3000','').replace('\t','').replace(']','').replace('[・|','')
    text=re.sub('\[([^|\]]+)\|','',text)#删除脚本中的注音标识
    return text

def hanzitihuan(text):#按照字典替换不支持的汉字，后续通过UniversalInjectorFramework替换回去以正常显示
    global target_chars,source_chars
    replaced_string=''
    for char in text:
        replaced_string += hanzidict.get(char, char)
        if char in hanzidict:
            if char not in target_chars:
                target_chars=target_chars+char
                source_chars=source_chars+hanzidict[char]
    return replaced_string

def fuhaotihuan(text):#替换掉译文中一些不支持的常见特殊符号形式，以正常显示
    return text.replace('—','ー').replace('～','〜').replace('“','「').replace('”','」').replace('·','・')

transpath='.\译文\Marguerite_strings.json'
with open(transpath,'r',encoding='utf-8') as f:
    trans=json.load(f)
namedicpath='.\OriginFile\\namelist.json'
with open(namedicpath,'r',encoding='utf-8') as f:
    namedic=json.load(f)

replacement_dict={}
for dic in trans:
    replacement_dict[teshuzifutihuan(dic["pre_jp"])]=dic["post_zh_preview"]
for name in namedic:
    replacement_dict[name]=namedic[name]

with codecs.open('.\OriginFile\Marguerite.txt', 'r', encoding='utf8') as input_file:
    with codecs.open(".\\fvp\\Marguerite_transed.txt", 'w', encoding='utf8') as hime:
        with codecs.open(".\\fvp\\Marguerite_strings_transed.txt", 'w', encoding='utf8') as himestrings:
            for line in input_file:
                if line.startswith("\tpushstring "):
                    content = line.strip()[11:]
                    content1 = teshuzifutihuan(content)
                    sline=content
                    if content1 in replacement_dict:
                        if len(content1)>0:
                            if not re.match(r'[A-Za-z]', content1[0]):#避免对调用资源文件的代码进行替换
                                if replacement_dict[content1]!="Failed translation":
                                    line = line.replace(content,replacement_dict[content1])
                                    sline= replacement_dict[content1]
                    himestrings.write(fuhaotihuan(hanzitihuan(sline))+'\n')
                hime.write(fuhaotihuan(hanzitihuan(line)))

import os
os.system('.\文本导入\封包.cmd')

with open('.\\Marguerite_chs\\uif_config.json','r',encoding='utf8',errors='ignore') as f:
    f=json.load(f)
    f["text_processor"]["rules"][0]["source_chars"]=source_chars
    f["text_processor"]["rules"][0]["target_chars"]=target_chars

with open('.\\Marguerite_chs\\uif_config.json','w',encoding='utf8') as fout:
    json.dump(f,fout,ensure_ascii=False,indent=4)

os.system('copy README.md Marguerite_chs\\')
os.system('del Marguerite_chs.rar')
os.system('Rar a -m0 Marguerite_chs.rar Marguerite_chs\\')