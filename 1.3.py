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

classfication = html_text.find_elements(by='xpath',value='//div[@class="css-4khqxp"]/text')
title = html_text.find_elements(by='xpath',value='//div[@class="css-3dzvwq"]/text')
adress = html_text.find_elements(by='xpath',value='//div[@class="css-15kzvwj"]/a[@href]')
hotnum = html_text.find_elements(by='xpath',value='//div[@class="css-3dx4z1"]/text')

result['classfication'].append(classfication)
result['title'].append(title)
result['adress'].append(adress)
result['hotnum'].append(hotnum)

ranking=list(range(1,101))

df=pd.DataFrame(result)
df.index=df.index+1
df.index.name='ranking'
df.to_csv('zhihu2.csv',encoding='utf-8-sig')