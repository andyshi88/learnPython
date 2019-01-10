'''
v01，初步爬取小说网站信息
碰见中文的乱码问题，可以使用 encoding解决
'''

import requests

if __name__ == '__main__':

    target = "https://www.kanunu8.com/book4/8583/188412.html"

    req = requests.get(url= target)

    # 在第一遍未解码时出现乱码，发现网站编码是gbk时，进行解码
    req.encoding = "gbk"

    print(req.text)

