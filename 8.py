import re
import urllib.request
import time
import urllib.error

headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 SE 2.X MetaSr 1.0')
opener = urllib.request.build_opener()
opener.addheaders=[headers]

urllib.request.install_opener(opener)

listurl=[]

def use_proxy(proxy_addr,url):
    try:
        import urllib.request
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data= urllib.request.urlopen(url).read().decode('utf-8')
        return data
        print(data)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

def getlisturl(key,pagestart,pageend,proxy):
    try:
        page=pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        #编码 “&page”
        pagecode=urllib.request.quote("&page")
        #循环爬取各页的文章链接
        for page in range(pagestart,pageend+1):
            #分别构建各页的url链接，每次循环构建一次
            url="http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)
            #用代理服务器爬去，解决封杀IP问题
            data1=use_proxy(proxy,url)
            #获取文章链接的正则表达式
            listurlpat='<div class="txt-box">.*?(http://.*?)"'
            #获取每页的所有文章链接并添加到列表listurl中
            listurl.append(re.compile(listurlpat,re.S).findall(data1))
        print("共获取到"+str(len(listurl))+"页") #便于调试
        return listurl
        print(listurl)
        print(data1)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若URLerror异常，则延迟10秒
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        #若为Exception异常，则延迟1秒
        time.sleep(1)

#获取文章内容
def getcontent(listurl,proxy):
    i=0
    #设置本地文件中的开始html编码
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1-transitional.dtd">
<html xmlns="http://w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=etf-8" />
<title>微信文章页面</title>
</head>
<body>'''
    fh=open("C:/Users/WangzyOwner/Desktop/1.html","wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    #再次以追加写入的方式打开文件，以写入对应的文章内容
    fh=open("C:/Users/WangzyOwner/Desktop/1.html","ab")
    #此时listurl为二维列表，形如listurl[][]，第一维储存的信息跟第几页相关，第二维储存的跟该页的第几个文章链接相关
    for i in range(0,len(listurl)):
 #   for i in range(0,100):
        for j in range(0,len(listurl[i])):
            try:
                url=listurl[i][j]
                #处理成真实url，去掉链接中一串amp
                url=url._replace("amp;","")
                #使用代理爬取对应网址的内容
                data=use_proxy(proxy,url)
                #文章标题正则表达式
                titlepat="<title>(.*?)</title>"
                #文章内容的正则表达式
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                #通过对应的表达式找到标题赋给title
                title=re.compile(titlepat).findall(data)
                #通过对应的正则表达式找到内容并赋给列表conten
                content=re.compile(contentpat,re.S).findall(data)
                #初始化标题与内容
                thistitle="此次没有获取到"
                thiscontent="此次没获取到"
                #如果列表不为空，说明找到了标题，取列表第零个元素，即此次标题赋给变量thistitle
                if(title!=[]):
                    thistitle=title[0]
                if(content!=[]):
                    thiscontent=content[0]
                #将标题与内容汇总赋给变量dataall
                dataall="<p>标题为:"+thistitle+"</p><p>内容为："+thiscontent+"</p><br>"
                #将该篇文章的标题与内容的总信息写入对应文件
                fh.write(dataall.endcode("utf-8"))
                print("第"+str(i)+"个网页的第"+str(j)+"次处理")#便于调试
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"readon"):
                    print(e.readon)
                time.sleep(10)
            except Exception as e:
                print("exception"+str(e))
                time.sleep(1)
    fh.close()
    #设置并写入本地文件的html后面结束部分代码
    html2='''</body>
</html>
            '''
    fh=open("C:/Users/WangzyOwner/Desktop/1.html","ab")
    fh.write(html2.encode("utf-8"))
    fh.close()

#设置关键词
key="物联网"
#设置代理服务器
proxy="123.249.28.188:3128"
proxy2=" "
#起始页
pagestart=1
#爬取到哪一页
pageend=2

listurl=getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)