import requests
import jsonpath
import json
import pandas as pd

url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&period=hour'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=headers)
#print(response)

result={
    'classfication':[],
    'title':[],
    'adress':[],
    'hotnum':[]
}
html_str=response.content.decode()
jsonobj=json.loads(html_str)

classfication=jsonpath.jsonpath(jsonobj,'$..name')
title=jsonpath.jsonpath(jsonobj,'$.data..title')
adress=jsonpath.jsonpath(jsonobj,'$..url')
hotnum=jsonpath.jsonpath(jsonobj,'$..score')

result['classfication'].append(classfication)
result['title'].append(title)
result['adress'].append(adress)
result['hotnum'].append(hotnum)

df=pd.DataFrame(result)
df.index=df.index+1
df.to_csv("知乎热榜.csv",encoding='utf-8-sig')