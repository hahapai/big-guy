import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/65.0.3325.162 Safari/537.36'
         }
url='http://www.sdsecurity.org.cn/news-18-1.html'
def  get_html(url):
    dd = requests.get(url,headers=headers)
    # print(dd.text)
    dd_text=dd.text
    results=re.findall(r'<li><i.*?class="i"></i><a href="(.*?)">.*?</a></li>',dd_text,re.S)
    ll='http://www.sdsecurity.org.cn/'
    kk = [ll + x for x in results]
    return kk
ll=get_html(url)
# print(ll)
def get_news():
    for i in ll:
        yoyo = requests.get(i,headers=headers)
        html = etree.HTML(yoyo.text)
        # yoyo_text=BeautifulSoup(yoyo.text,"lxml")
        # news=yoyo_text.select("body .web_widht main back_white clearfix .listConts .title")
        html_data = html.xpath('/html/body/div/div/h1/text()')
        # get_title = re.findall(r'<h1 class="title">(.*?)</h1>',yoyo_text,re.S)
        get_comment = html.xpath('//*[@id="textarea"]/table/tbody/tr/td/p/span/text()')
        str1 = (''.join(get_comment))
        print(html_data)
        print(str1)
get_news()