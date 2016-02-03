#-*-coding:utf-8-*- 

import os
import uuid
import urllib.request
import http.cookiejar

#获取文件后缀名
def get_file_extension(file):  
    return os.path.splitext(file)[1]  

#创建文件目录，并返回该目录
def mkdir(path):
    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)
        
    return path

#自动生成一个唯一的字符串
def unique_str():
    return str(uuid.uuid1())

#抓取网页文件内容，保存到内存 url欲抓取文件 ，path+filename
def get_file(url):
    try:
        cj=http.cookiejar.LWPCookieJar()
        opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        
        req=urllib.request.Request(url)
        operate=opener.open(req)
        data=operate.read()
        return data
    except BaseException as e:
        print(e)
        return None
    
#保存文件到本地 path本地路径  file_name文件名  data文件内容
def save_file(path, file_name, data):
    if data == None:
        return
    
    mkdir(path)
    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()
 

#获取文件后缀名
print(get_file_extension("123.jpg"));

#创建文件目录，并返回该目录
#print mkdir("d:/python")

#自动生成一个唯一的字符串
print(unique_str())

url="http://cn.bing.com/images?FORM=Z9LH";
save_file("d:/python/", "123.jpg", get_file(url))
