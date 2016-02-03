# -*-coding:utf-8-*-
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    #正则匹配
    reg = r'src="(.+?\.jpg|png|gif)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    #遍历图片
    for imgurl in imglist:
        #保存图片并重命名
        urllib.request.urlretrieve(imgurl,'d:\\print\%s' % x)
        x+=1


html = getHtml("http://www.qq.com/")
#网页编译方式


print(getImg(html))
