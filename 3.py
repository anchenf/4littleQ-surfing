import requests
import pandas as pd
import bs4
from urllib import parse
import time
import datetime

result={
    'full_adress':[],
    'name':[],
    'Itime':[]
}

url='https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM=1&urltype=tree.TreeTempUrl&wbtreeid=1010'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
response=requests.get(url=url,headers=headers)

soup=bs4.BeautifulSoup(response.text,'html.parser')
a_list = soup.find_all('div',class_="leftNews3")
for i in a_list:
    adress_f = i.find('a')['href']
    name = i.find('a').text
    Itime=i.find('div',style="float:right;").text

    base_adress='https://www.bkjx.sdu.edu.cn/'
    full_adress=parse.urljoin(base=base_adress,url=adress_f,allow_fragments=True)

    result['full_adress'].append(full_adress)
    result['name'].append(name)
    result['Itime'].append(Itime)


df=pd.DataFrame(result)
df.index=df.index+1
df.to_csv('School_Information.csv',encoding='utf-8-sig')


if __name__ == '__main__':

    flag = 0
    now = datetime.datetime.now()

    sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
                                    now.second) + datetime.timedelta(seconds=5)

    while (True):
        now = datetime.datetime.now()
        if sched_timer < now < sched_timer + datetime.timedelta(seconds=1):
            time.sleep(1)
            print(now)
            # 运行程序

            # 将标签设为 1
            flag = 1
        else:
            # 标签控制 表示主程序已运行，才修改定时任务时间
            if flag == 1:
                # 修改定时任务时间 时间间隔为24小时
                sched_timer = sched_timer + datetime.timedelta(minutes=2)
                flag = 0