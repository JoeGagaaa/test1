import re
import urllib.request

"""
file = urllib.request.urlopen("https://www.baidu.com/s?wd")
url="https://www.baidu.com/s?wd"
key = "python"
key_code =urllib.request.quote(key)
url_all = url+key_code
req = urllib.request.Request(url_all)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
data = urllib.request.urlopen(req).read()

file = open("C:/Users/WangzyOwner/Desktop/1.html","wb")
file.write(data)
file.close

"""


def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+?<div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    print (result1)
    result1=result1[0]
    print(result1)
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename="C:/Users/WangzyOwner/Desktop/jdimg/"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(0,1):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

