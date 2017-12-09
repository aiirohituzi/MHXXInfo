from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import xlsxwriter
import config

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)

data = []

for num in config.QUESTNUM:
    print(num)
    driver.get('http://wiki.mhxg.org/ida/' + num + '.html')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # questName = soup.select(
    #     '#quest' + num + ' > div > div.panel-heading > a:nth-of-type(2)'
    # )
    
    # questMap = soup.select(
    #     '#quest' + num + ' > div > div.panel-body.view_panel_body.a_cl21913' + str(i) + ' > a'
    # )

    questName = soup.select(
        '#id' + num + ' > td'
    )

    rating = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > h3'
    )

    questMap = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(2) > a'
    )

    questTime = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(1) > td:nth-of-type(3)'
    )

    condition_main = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(1) > td:nth-of-type(1)'
    )

    condition_sub = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(1) > td:nth-of-type(2)'
    )

    down_payment = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(3)'
    )

    rewardMoney_main = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(1)'
    )

    rewardMoney_sub = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > table:nth-of-type(2) > tbody > tr:nth-of-type(2) > td:nth-of-type(2)'
    )

    # print(questName)
    # print(questMap)
    # print(questTime)
    # print(condition_main)
    # print(condition_sub)
    # print(down_payment)
    # print(rewardMoney_main)
    # print(rewardMoney_sub)
    # print('--------------')

    data.append({
        'questName': questName[0].text.replace("\n", "").rstrip().lstrip(),
        'rating': rating[0].text.replace(questName[0].text.replace("\n", "").rstrip().lstrip(), ""),
        'questMap' : questMap[0].text,
        'questTime' : questTime[0].text,
        'condition_main' : condition_main[0].text,
        'condition_sub' : condition_sub[0].text,
        'down_payment' : down_payment[0].text,
        'rewardMoney_main' : rewardMoney_main[0].text,
        'rewardMoney_sub' : rewardMoney_sub[0].text,
    })


driver.close()
# data = json.dumps(data, indent=4)
# print(data)



# f = open("data.txt", 'w', encoding='utf8')

# for q in data:
#     print(q.get('questName'))
#     print(q.get('questMap'))
#     f.write(q.get('questName') + ' / ' + q.get('questMap') + '\n')
# f.close()


worksheet.write('A1', 'questName')
worksheet.write('B1', 'rating')
worksheet.write('C1', 'questMap')
worksheet.write('D1', 'questTime')
worksheet.write('E1', 'condition_main')
worksheet.write('F1', 'condition_sub')
worksheet.write('G1', 'down_payment')
worksheet.write('H1', 'rewardMoney_main')
worksheet.write('I1', 'rewardMoney_sub')

row = 1
col = 0

for a in (data):
    worksheet.write(row, col, a.get('questName'))
    worksheet.write(row, col + 1, a.get('rating'))
    worksheet.write(row, col + 2, a.get('questMap'))
    worksheet.write(row, col + 3, a.get('questTime'))
    worksheet.write(row, col + 4, a.get('condition_main'))
    worksheet.write(row, col + 5, a.get('condition_sub'))
    worksheet.write(row, col + 6, a.get('down_payment'))
    worksheet.write(row, col + 7, a.get('rewardMoney_main'))
    worksheet.write(row, col + 8, a.get('rewardMoney_sub'))
    row += 1

workbook.close()