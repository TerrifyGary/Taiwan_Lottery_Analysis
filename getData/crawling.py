from bs4 import BeautifulSoup
import requests
import pandas

def hadleDate(soup):
    cleanDate = []
    filterDate = soup.find_all('td',attrs={'style':'font-size: 6vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom'})
    for i in filterDate:
        x = i.text
        x = x[:10]
        cleanDate.append(x)
    return cleanDate

def hadleLottoNumber(soup):
    cleanLottoNumber = []
    filterNumber = soup.find_all('td',attrs={'style':'font-size: 6vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC;text-align:center;padding:0px;vertical-align:middle'})
    for i in filterNumber:
        x = "".join((i.text.strip()).split()) 
        cleanLottoNumber.append(x)
    return cleanLottoNumber

def getPageData(webURL):
    date = []
    lottoNumber = []
    r = requests.get(url=webURL)
    checkStatusCode = int(r.status_code)

    if checkStatusCode==200:
        soup = BeautifulSoup(r.text, 'html.parser')
        date += hadleDate(soup)
        lottoNumber += hadleLottoNumber(soup)

    return date,lottoNumber