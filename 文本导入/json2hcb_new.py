#封包用,测试版,使用新的字符替换方法以避免错误替换
import codecs
import re
import json
from HanziReplacer import *

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

for i in replacement_dict:#生成hanzidict
    tempdict,charlist=GetInvalidChars(replacement_dict[i],tempdict,charlist)
hanzidict,target_chars,source_chars=Createhanzidict(tempdict,charlist)

with codecs.open('.\OriginFile\Marguerite.txt', 'r', encoding='utf8') as input_file:
    with codecs.open(".\\fvp\\Marguerite_transed.txt", 'w', encoding='utf8') as output:
        with codecs.open(".\\fvp\\Marguerite_strings_transed.txt", 'w', encoding='utf8') as outputstrings:
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
                    outputstrings.write(hanzitihuan(fuhaotihuan(sline),hanzidict)+'\n')
                output.write(hanzitihuan(fuhaotihuan(line),hanzidict))

import os
os.system('.\文本导入\封包.cmd')

UFIConfigpath='.\\Marguerite_chs\\uif_config.json'
ChangeUFIConfig(UFIConfigpath,source_chars,target_chars)

os.system('copy README.md Marguerite_chs\\')
os.system('del Marguerite_chs.rar')
os.system('Rar a -m0 Marguerite_chs.rar Marguerite_chs\\')