import urllib
#import urllib2
import re
import pandas as pd
a=[]
url='http://focus.tianya.cn/'
request=urllib.Request(url)
response=urllib.urlopen(request)
content=response.read().decode('utf-8')
pattern=re.compile('<h3>.*?title="(.*?)".*?title" >',re.S)
items=re.findall(pattern,content)
for item in items:
    a.append(item)
    b=pd.DataFrame(a)
print (b)
