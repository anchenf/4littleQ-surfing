from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.chrome.options import Options #无界面浏览器
from selenium.webdriver import ChromeOptions#规避检测

result={
    'classfication':[],
    'title':[],
    'adress':[],
    'hotnum':[]
}


edge_options=Options()
edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument('blink-settings=imagesEnabled=false')
delay=5
path='msedgedriver.exe'
browser=webdriver.Edge(path)
browser.set_page_load_timeout(40)
browser.set_script_timeout(40)

html_text=browser.page_source

url='https://www.zhihu.com/knowledge-plan/hot-question/hot/0/hour/'
browser.get(url)
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
opt=webdriver.EdgeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
browser=webdriver.Edge(options=opt)


WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.XPATH,"//div[@class='css-4khqxp']")))
WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='css-3dzvwq']")))
WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='css-15kzvwj']/a[@href]")))
WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='css-3dx4z1']")))
classfication = browser.find_elements(by='xpath',value='//div[@class="css-4khqxp"]/text')
title = browser.find_elements(by='xpath',value='//div[@class="css-3dzvwq"]/text')
adress=browser.find_elements(by='xpath',value='//div[@class="css-15kzvwj"]/a[@href]')
hotnum = browser.find_elements(by='xpath',value='//div[@class="css-3dx4z1"]/text')


for a in classfication:
    result['classfication'].append(a.text)

for b in title:
    result['title'].append(b.text)

for c in adress:
    result['adress'].append(adress)

for d in hotnum:
    result['hotnum'].append(hotnum.text)


ranking=list(range(1,101))
while ranking>100:
    print('加载完毕')
    break


df=pd.DataFrame(result)
df.index=df.index+1
df.index.name='ranking'
df.to_csv('zhihu2.csv',encoding='utf-8-sig')