# coding=utf-8
from bs4 import BeautifulSoup
import requests

allDateInfo = []
allResultInfo = []

def getLottery(date,result,url):
    r = requests.get(url) 
    isConnected = int(r.status_code) # 檢查status code是否為200
    temp = []
    if (isConnected==200):
        soup = BeautifulSoup(r.text, 'html.parser') # 抓取html
        filterDate = soup.find_all('td', attrs={'style':'font-size: 4vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC;text-align:center;padding:0px;vertical-align:middle'})
        filterNumb = soup.find_all('td', attrs={'style':'font-size: 6vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC;text-align:center;padding:0px;vertical-align:middle'})
        for i,j in zip(filterDate,filterNumb):
            x = i.text.strip()
            y = j.text.strip() # strip() 可以去除頭尾的空白鍵
            date.append(x)
            temp.append(y)
        for i in temp:
            x = "".join(i.split())
            # print(x)
            result.append(x)

def getPagesInfo(date,result,num):
    for i in range (num):
        url = 'https://www.pilio.idv.tw/lto539/list.asp?indexpage=%s&orderby=new'%(191-num)
        getLottery(date, result, url)
    
    return date, result
allDateInfo,allResultInfo = getPagesInfo(allDateInfo,allResultInfo,10)
print(allDateInfo, allResultInfo)