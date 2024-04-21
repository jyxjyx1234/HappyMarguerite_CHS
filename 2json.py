#本文件用于将hcb拆包得到的txt文件转化为galtransl所需的json文件
import json  
import re

# 定义输入和输出文件的名字  
input_filename = ".\OriginFile\Marguerite_strings.txt"
output_filename = ".\OriginFile\Marguerite_strings.json"
namelist_filename = ".\OriginFile\\namelist.json"
def zhuyinchuli(text):#处理注音（已经在文本编辑器中处理过了,这里不再进行处理）
    text=re.sub('\[[^\[]*\|','',text)
    return text.replace("]","")

# 初始化一个空列表来存储消息  
messages = []
  
# 打开输入文件并逐行读取  
with open(input_filename, 'r', encoding='sjis') as file:
    i={}
    jilu=[]#去除重复语句以省钱
    namelist={}
    for line in file:
        if "【" in line:
            i['name']=line.replace("【",'').replace("】",'').replace("\n",'')
            if i['name'] not in namelist:
                namelist[i['name']]=''
        else:
            i['message']=line.replace("\n",'')
            if i['message'] not in jilu:
                jilu.append(i['message'])
                messages.append(i)
            i={}
        
  
# 将消息列表写入JSON文件  
with open(output_filename, 'w', encoding='UTF-8') as json_file:  
    json.dump(messages, json_file, ensure_ascii=False, indent=4)  
with open(namelist_filename, 'w', encoding='UTF-8') as json_file:  
    json.dump(namelist, json_file, ensure_ascii=False, indent=4)

for i in namelist:
    print(i)
