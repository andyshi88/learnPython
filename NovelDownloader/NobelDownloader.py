'''
思路整理
1，先爬取目录网页，得到每个章节的URL
2，再通过每个章节的URL，爬取每个章节的内容
3，写入文本
'''

from bs4 import BeautifulSoup
import requests, sys

# 定义一个下载器的类
class downloader(object):

    def __init__(self):
        self.server = "https://www.kanunu8.com/book4/8583/"
        self.target = "https://www.kanunu8.com/book4/8583/index.html"

        self.names = []     # 存放章节名
        self.urls = []      # 存放章节连接
        self.nums = 0       # 存放章节数

    # 获取每个章节的URL
    def get_download_urls(self):
        req = requests.get(url= self.target)
        req.encoding = "gb2312"
        html = req.text
        soup = BeautifulSoup(html)
        tr_soup = soup.find_all('table', border="0", cellspacing="1", cellpadding="8", width="800", align="center")
        a_soup = BeautifulSoup(str(tr_soup[0]))
        a = a_soup.find_all('a')
        self.nums = len(a)
        for item in a:
            self.names.append(item.string)
            self.urls.append(self.server + item.get("href"))

        # 自动添加到list中，无需返回值

    # 获取每个章节的内容
    def get_contents(self, target):
        req = requests.get(url= target)
        req.encoding = "gbk"
        html = req.text
        soup = BeautifulSoup(html)
        texts = soup.find_all('p')
        texts = texts[0].text.replace('\xa0'*4,'\n')
        return texts

    # 将爬取的内容写入到文件
    def writer(self, name , path, text):
        '''
        :param name: 章节名称
        :param path: 保存路径
        :param text: 章节内容
        :return: None
        '''
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_urls()
    print("《狼图腾》正在下载：")
    for i in range(dl.nums):
        dl.writer(dl.names[i], '狼图腾.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print("《狼图腾》下载完成")
