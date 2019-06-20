import urllib.request


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
#data =file.read()

#dataline = file.readline()
#filename = urllib.request.urlretrieve("https://www.zhipin.com/",filename = "C:/Users/WangzyOwner/Desktop/1.html")
#fhandle= open("C:\Users\WangzyOwner\Desktop\1.html","wb")
#fhandle.write(data)
#fhandle.close()
#print(dataline)
#print(data)