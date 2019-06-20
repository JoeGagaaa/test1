import re
import urllib.request

def getlink(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 SE 2.X MetaSr 1.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    #file.raise_for_status()
    data = str(file.read)

    pat='(https?://[^\s)";]+\.(\w|/)*)'
    link=re.compile(pat).findall(data)
    print(link)
    link=list(set(link))
    print(link)
    return link

url="http://blog.csdn.net/"
linklist=getlink(url)
#print("1")
#print(link)
"""
for link in linklist:
    printf(link[0])
    printf('1')
"""

"""
file = open("C:/Users/WangzyOwner/Desktop/1.txt")
    file.write(link[0])
    file.close

"""