'''
根据03中的结果，提取每个a标签中的连接和内容
'''

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    server = "https://www.kanunu8.com/book4/8583/"
    target = "https://www.kanunu8.com/book4/8583/index.html"

    req = requests.get(url= target)

    req.encoding = "gb2312"

    html = req.text

    soup = BeautifulSoup(html)

    tr_soup = soup.find_all('table', border="0", cellspacing="1", cellpadding="8", width="800", align="center")

    a_soup = BeautifulSoup(str(tr_soup[0]))

    a = a_soup.find_all('a')

    for item in a:
        print(item.string, server + item.get('href'))

