import requests
import pandas as pd

url="https://www.zhihu.com/knowledge-plan/hot-question/hot/100029/hour"

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response=requests.get(url=url,headers=headers).json()


df = pd.DataFrame(columns=['热点分类','标题','链接','热力值'])



for dict in response['list']:
    classfication=[]
    title=[]
    href=[]
    hotnum=[]

    classfication.append(dict['classfication'])
    title.append(dict['title'])
    href.append(dict['href'])
    hotnum.append(dict['hotnum'])

dict={'热点分类':classfication,'标题':title,'链接':href,'热力值':hotnum}


df.index=df.index+1


df.to_csv('zhihu.csv',encoding='utf-8')