from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

result={
    'classfication':[],
    'title':[],
    'adress':[],
    'hotnum':[]
}

path='msedgedriver.exe'
browser=webdriver.Edge(path)

url='https://www.zhihu.com/knowledge-plan/hot-question/hot/0/hour'

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

opt=webdriver.EdgeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
browser=webdriver.Edge(options=opt)
browser.get(url)
html_text=browser.page_source
soup=BeautifulSoup(html_text,'html.parser')


for title in soup.find_all('div',class_="css-3dzvwq"):
    result['title'].append(title)


adress_list=soup.find_all('div',class_="css-15kzvwj")
for i in adress_list:
    adress = i.find('a')["href"]
    result['adress'].append(adress)

b_list=soup.find_all('div',class_="css-4khqxp")
for j in b_list:
    classfication=j.find_next('a').text
    result['classfication'].append(classfication)

for hotnum in soup.find_all('div',class_="css-3dx4z1"):
    result['hotnum'].append(hotnum)

ranking=list(range(1,101))

df=pd.DataFrame(result)
df.index=df.index+1
df.index.name='ranking'
df.to_csv('zhihu2.csv',encoding='utf-8-sig')