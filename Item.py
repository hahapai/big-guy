import requests
from pyquery import PyQuery as pq
import os, sys

os.chdir('D:/work')


def crawle():
    url = 'https://www.qtshu.com/zetianji/'
    req = requests.get(url=url)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    # 初始化pyquery对象
    doc = pq(html)
    # 传入css选择器
    items = doc('.booklist ul li').items()
    # m和index是为了计算进度
    m = len(doc('.booklist ul li'))
    index = 1
    fr = open('择天记.txt', 'w')
    print('*' * 100)
    print(' ' * 50, '欢迎学习交流')
    print('*' * 100)
    for each in items:
        title = each.text()
        url = each.find('a').attr('href')
        # 有的没有url
        if url:
            index += 1
            url = 'https://www.qtshu.com/zetianji/' + url
            # print(title,url)
            text = Text(url)
            fr.write(title)
            fr.write('\n\n')
            fr.write(text)
            fr.write('\n\n')
            # 进度条显示
            print( '已下载:%.3f%%' % float(index / m) + '\r')

            # sys.stdout.write('已下载:%.3f%%' % float(index / m) + '\r')
            # sys.stdout.flush()


from bs4 import BeautifulSoup


def Text(url):
    req = requests.get(url=url)
    req.encoding = 'utf-8'
    html = req.text
    doc = pq(html)
    item = doc('.contentbox p').text()
    if '\ufeff' in item:
        item = item.replace('\ufeff', '')
    if '\xa0' in item:
        item = item.replace('\xa0', '')
    return item


crawle()