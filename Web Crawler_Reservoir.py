import time
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

dam=['石門水庫','翡翠水庫','寶山第二水庫','永和山水庫','明德水庫','鯉魚潭水庫',
     '德基水庫','石岡壩','霧社水庫','日月潭水庫','集集攔河堰','湖山水庫','仁義潭水庫',
     '白河水庫','烏山頭水庫','曾文水庫','南化水庫','阿公店水庫','高屏溪攔河堰','牡丹水庫']
csvfile=open("20190225.csv","w",newline='')
writer=csv.writer(csvfile)
writer.writerow(['水庫名稱','日期','進流量','水位','有效蓄水量','蓄水百分比'])

for i in range(2003,2020,1):
    for j in range(1,13,1):
        browser1 = webdriver.Chrome()
        browser1.get("http://fhy.wra.gov.tw/ReservoirPage_2011/Statistics.aspx")
        element_year = browser1.find_element_by_id("ctl00_cphMain_ucDate_cboYear")
        element_month = browser1.find_element_by_id("ctl00_cphMain_ucDate_cboMonth")
        element_day = browser1.find_element_by_id("ctl00_cphMain_ucDate_cboDay")
        element_hour = browser1.find_element_by_id("ctl00_cphMain_ucDate_cboHour")
        element_minute = browser1.find_element_by_id("ctl00_cphMain_ucDate_cboMinute")
        element_query = browser1.find_element_by_id("ctl00_cphMain_btnQuery")
        element_year.send_keys(str(i))
        mon=str(j)
        time.sleep(1)
        element_month.send_keys(mon)
        element_day.send_keys('15')
        element_hour.send_keys('0')
        element_minute.send_keys('0')
        element_query.click()
        time.sleep(2)
        ht=browser1.page_source
        soup = BeautifulSoup(ht,"html.parser")
        stories = soup.find_all('td')
        num=0
        print("月份：",mon)
        print()
        for d in dam:
            print(d,stories[num+1].string,stories[num+3].string,stories[num+4].string,stories[num+6].string,stories[num+7].string)
            writer.writerow([d,stories[num+1].string,stories[num+3].string,stories[num+4].string,stories[num+6].string,stories[num+7].string])
            num += 17
        print()
        browser1.quit()
csvfile.close()
