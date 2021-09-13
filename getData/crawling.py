from bs4 import BeautifulSoup
import requests
import pandas

page = 100
def hadleDate(soup):
    cleanDate = []
    filterDate = soup.find_all('td',attrs={'style':'font-size: 4vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC;text-align:center;padding:0px;vertical-align:middle'})
    for i in filterDate:
        x = i.text
        x = x[:10]
        cleanDate.append(x)
    cleanDate.reverse()
    return cleanDate

def hadleLottoNumber(soup):
    cleanLottoNumber = []
    filterNumber = soup.find_all('td',attrs={'style':'font-size: 6vmin; font-weight: bold; color: #000000;border-bottom-style: dotted; border-bottom-color: #CCCCCC;text-align:center;padding:0px;vertical-align:middle'})
    for i in filterNumber:
        x = "".join((i.text.strip()).split()) 
        cleanLottoNumber.append(x)
    cleanLottoNumber.reverse()
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

def getMorePages(num):
    tempAllPageDate = []
    tempAllPageLottoNumber = []

    for i in range (num):
        pageURL = f'https://www.pilio.idv.tw/lto539/list.asp?indexpage={191-i}&orderby=new'
        tempAllPageDate += getPageData(webURL=pageURL)[0]
        tempAllPageLottoNumber += getPageData(webURL=pageURL)[1]
        print(f'It is now page Number {i+1}.')

    return tempAllPageDate, tempAllPageLottoNumber

allPageDate, allPageLottoNumber = getMorePages(page)
dict = {'date': allPageDate,'lottoNumber':allPageLottoNumber}
dataFrame = pandas.DataFrame(dict)
dataFrame.to_csv('output.csv')
