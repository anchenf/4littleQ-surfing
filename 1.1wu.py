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




classfication=browser.find_elements(by='xpath',value='//div[@class="css-4khqxp"]')
title=browser.find_elements(by='xpath',value='//div[@class="css-3dzvwq"]')
adress=browser.find_elements(by='xpath',value='//div[@class="css-15kzvwj"]/a[@href]')
hotnum=browser.find_elements(by='xpath',value='//div[@class="css-3dx4z1"]')