from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)

data = []

ratings = {}

driver.get('http://wiki.mhxg.org/data/2011.html')



html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')



for i in range(3, 8):
    questName = soup.select(
        '#quest21913' + str(i) + ' > div > div.panel-heading > a:nth-of-type(2)'
    )
    
    questMap = soup.select(
        '#quest21913' + str(i) + ' > div > div.panel-body.view_panel_body.a_cl21913' + str(i) + ' > a'
    )
    # print(questName[0].text)
    data.append({
        'questName': questName[0].text,
        'questMap' : questMap[0].text
    })

# data = json.dumps(data, indent=4)
print(data)



f = open("data.txt", 'w', encoding='utf8')

for q in data:
    print(q.get('questName'))
    print(q.get('questMap'))
    f.write(q.get('questName') + ' / ' + q.get('questMap') + '\n')
f.close()

driver.close()