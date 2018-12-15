import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv
csvfile=open("20181103v2.csv","w",newline='')
csvfile_year=open("20181103year.csv","w",newline='')
writer_year=csv.writer(csvfile_year)
writer=csv.writer(csvfile)
writer.writerow(['年份','月份','測站','雨量'])
writer_year.writerow(['年份','測站','雨量'])

for y in range(1998,2019):
    rainfallsum={}
    for m in range(1,13):
        urlstr="https://www.cwb.gov.tw/V7/climate/monthlyData/Data/mD"+str(y)+str(m)+".htm"
        print(urlstr)
        page=urllib.request.urlopen(urlstr).read()
        soup=BeautifulSoup(page,"html.parser")
        stories = soup.find_all('td')
        j=14
        sum_j=0
        print("length=",len(stories))
        for i in stories:
            print(j,stories[j].text,stories[j+4].text)
            writer.writerow([y,m,stories[j].text,stories[j+4].text])
            if m==1 or rainfallsum.get(stories[j].text)==None:
                rainfallsum[stories[j].text]=0
            if stories[j+4].text=='T' or stories[j+4].text=='':
                rainfallsum[stories[j].text]=rainfallsum[stories[j].text]+0
            else:
                rainfallsum[stories[j].text]=rainfallsum[stories[j].text]+round(float(stories[j+4].text),1)
            if m==12:
                writer_year.writerow([y,stories[j].text,rainfallsum[stories[j].text]])
            if j+13 < len(stories):
                j=j+12
                sum_j=sum_j+1
                print("j=",j)
            else:
                break
#           writer_year.writerow([y,stories[j].text,rainfallsum])
        if y==2018 and m==10:
            break
csvfile.close()
csvfile_year.close()
