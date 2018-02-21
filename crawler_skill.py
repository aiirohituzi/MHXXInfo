from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import xlsxwriter
import config_skill

workbook = xlsxwriter.Workbook('skill.xlsx')
worksheet = workbook.add_worksheet()

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=chrome_options)

data = []

for num in config_skill.SKILL_NUM:
    print(num)
    driver.get('http://wiki.mhxg.org/ida/' + num + '.html')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    skillName = ''
    point = ''
    effect = ''

    skillType = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td:nth-of-type(2)'
    )

    skillName1 = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td:nth-of-type(3) > span'
    )
    point1 = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td:nth-of-type(4) > span'
    )
    effect1 = soup.select(
        '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td:nth-of-type(5) > span'
    )

    skillName = skillName1[0].text
    point = point1[0].text
    effect = effect1[0].text

    if num in config_skill.SKILL_TWO_NUM:
        skillName2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(1) > span'
        )
        point2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span'
        )
        effect2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(3) > span'
        )
        skillName = skillName + '/' + skillName2[0].text
        point = point + '/' + point2[0].text
        effect = effect + '/' + effect2[0].text

    if num in config_skill.SKILL_THREE_NUM:
        skillName2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(1) > span'
        )
        point2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span'
        )
        effect2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(3) > span'
        )
        skillName3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(1) > span'
        )
        point3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(2) > span'
        )
        effect3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(3) > span'
        )
        skillName = skillName + '/' + skillName2[0].text + '/' + skillName3[0].text
        point = point + '/' + point2[0].text + '/' + point3[0].text
        effect = effect + '/' + effect2[0].text + '/' + effect3[0].text

    if num in config_skill.SKILL_FOUR_NUM:
        skillName2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(1) > span'
        )
        point2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span'
        )
        effect2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(3) > span'
        )
        skillName3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(1) > span'
        )
        point3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(2) > span'
        )
        effect3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(3) > span'
        )
        skillName4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(1) > span'
        )
        point4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(2) > span'
        )
        effect4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(3) > span'
        )
        skillName = skillName + '/' + skillName2[0].text + '/' + skillName3[0].text + '/' + skillName4[0].text
        point = point + '/' + point2[0].text + '/' + point3[0].text + '/' + point4[0].text
        effect = effect + '/' + effect2[0].text + '/' + effect3[0].text + '/' + effect4[0].text

    if num in config_skill.SKILL_FIVE_NUM:
        skillName2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(1) > span'
        )
        point2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span'
        )
        effect2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(3) > span'
        )
        skillName3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(1) > span'
        )
        point3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(2) > span'
        )
        effect3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(3) > span'
        )
        skillName4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(1) > span'
        )
        point4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(2) > span'
        )
        effect4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(3) > span'
        )
        skillName5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(1) > span'
        )
        point5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(2) > span'
        )
        effect5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(3) > span'
        )
        skillName = skillName + '/' + skillName2[0].text + '/' + skillName3[0].text + '/' + skillName4[0].text + '/' + skillName5[0].text
        point = point + '/' + point2[0].text + '/' + point3[0].text + '/' + point4[0].text + '/' + point5[0].text
        effect = effect + '/' + effect2[0].text + '/' + effect3[0].text + '/' + effect4[0].text + '/' + effect5[0].text

    if num in config_skill.SKILL_SIX_NUM:
        skillName2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(1) > span'
        )
        point2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span'
        )
        effect2 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(3) > td:nth-of-type(3) > span'
        )
        skillName3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(1) > span'
        )
        point3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(2) > span'
        )
        effect3 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(4) > td:nth-of-type(3) > span'
        )
        skillName4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(1) > span'
        )
        point4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(2) > span'
        )
        effect4 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(5) > td:nth-of-type(3) > span'
        )
        skillName5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(1) > span'
        )
        point5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(2) > span'
        )
        effect5 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(6) > td:nth-of-type(3) > span'
        )
        skillName6 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(7) > td:nth-of-type(1) > span'
        )
        point6 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(7) > td:nth-of-type(2) > span'
        )
        effect6 = soup.select(
            '#main_1 > div > div.row_x > div.col-md-10 > div > table:nth-of-type(1) > tbody > tr:nth-of-type(7) > td:nth-of-type(3) > span'
        )
        skillName = skillName + '/' + skillName2[0].text + '/' + skillName3[0].text + '/' + skillName4[0].text + '/' + skillName5[0].text + '/' + skillName6[0].text
        point = point + '/' + point2[0].text + '/' + point3[0].text + '/' + point4[0].text + '/' + point5[0].text + '/' + point6[0].text
        effect = effect + '/' + effect2[0].text + '/' + effect3[0].text + '/' + effect4[0].text + '/' + effect5[0].text + '/' + effect6[0].text





    print('skillType : ' + skillType[0].text.replace("[XX]", "").rstrip().lstrip())
    print('skillName : ' + skillName)
    print('point : ' + point)
    print('effect : ' + effect)
    # print('skillName1 : ' + skillName1[0].text)
    # print('skillName2 : ' + skillName2[0].text)
    # print('skillName3 : ' + skillName3[0].text)
    # print('skillName4 : ' + skillName4[0].text)
    # print('skillName5 : ' + skillName5[0].text)
    # print('skillName6 : ' + skillName6[0].text)
    # print('point1 : ' + point1[0].text)
    # print('point2 : ' + point2[0].text)
    # print('point3 : ' + point3[0].text)
    # print('point4 : ' + point4[0].text)
    # print('point5 : ' + point5[0].text)
    # print('point6 : ' + point6[0].text)
    # print('effect1 : ' + effect1[0].text)
    # print('effect2 : ' + effect2[0].text)
    # print('effect3 : ' + effect3[0].text)
    # print('effect4 : ' + effect4[0].text)
    # print('effect5 : ' + effect5[0].text)
    # print('effect6 : ' + effect6[0].text)

    data.append({
        'skillType': skillType[0].text.replace("[XX]", "").rstrip().lstrip(),
        'skillName': skillName,
        'point': point,
        'effect': effect
    })



driver.close()
# data = json.dumps(data, indent=4)
# print(data)


worksheet.write('A1', 'skillType')
worksheet.write('B1', 'skillName')
worksheet.write('C1', 'point')
worksheet.write('D1', 'effect')
row = 1
col = 0

for a in (data):
    worksheet.write(row, col, a.get('skillType'))
    worksheet.write(row, col + 1, a.get('skillName'))
    worksheet.write(row, col + 2, a.get('point'))
    worksheet.write(row, col + 3, a.get('effect'))
    row += 1


workbook.close()