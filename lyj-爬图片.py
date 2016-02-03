# -*-coding:utf-8-*-
import re
import os
import time
import urllib.request

def get_urls(url):
    html = urllib.request.urlopen(url).read()
    picurl = re.compile(r'<img alt=".+?"src="(.+?)"/><br/>')
    picts = picurl.findall(html)
    for urls in picts:
        try:
            name = re.sub(':','_',time.ctime()
                          [10:19])+'.jpg'
            print(name)
            urllib.request.urlretrieve(urls,'d:\\print'+name)
        except urllib.request.contentTooshortError as e:
                print(name+'failt')
                continue
def get_href(page):
    s = urllib.request.urlopen(page)
    hrefs = re.compile(r'<h2><a href="(.+?)".+?</a></h2>')
    s = s.read()
    links = hrefs.findall(s)
    return links

def main():
    for i in range(1,67):
        a = 'http://cn.bing.com/images?FORM=Z9LH'%i
        href = get_href(a)
        time.sleep(1)
        for j in href:
            get_urls(j)


if __name__=='__main__':
    os.chdir('d:\\print')
    main()
