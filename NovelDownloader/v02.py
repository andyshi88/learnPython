'''
在v01中，发现我们想要的内容比较简单，就在<p>段落中
下面我们就先把内容提取出来，用beautifulsoup
'''
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    target = "https://www.kanunu8.com/book4/8583/188412.html"

    req = requests.get(url= target)

    req.encoding = "gbk"

    html = req.text

    soup = BeautifulSoup(html)

    texts = soup.find_all('p')

    print(type(texts))

    print(texts[0].text.replace('\xa0'*4,'\n'))
