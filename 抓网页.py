# -*-coding:utf-8-*-
import urllib.request
def callbackfunc(blocknum,blocksize,totalsize):
    percent = 100.0*blocknum*blocksize/totalsize
    if percent>100:
        percent = 100
    print("%.2f%%"% percent)
def getdata():
    url = 'http://www.sina.com.cn'
    local = 'd:\\print\'
    data = urllib.request.urlretrieve(url,local,callbackfunc)
    z_data = data.decode('UTF-8')
    print(z_data)
getdata()
