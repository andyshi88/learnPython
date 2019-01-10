'''
v03分析小说的目录发现每个章节的目录在<tr bgcolor="#ffffff">的表格中
下面就来提前每个章节的连接地址
'''
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    target = "https://www.kanunu8.com/book4/8583/index.html"

    req = requests.get(url= target)

    req.encoding = "gb2312"

    html = req.text

    soup = BeautifulSoup(html)

    text = soup.find_all('table', border="0", cellspacing="1", cellpadding="8", width="800", align="center")

    print(text)

