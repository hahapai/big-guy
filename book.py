import urllib.request
import re
#http://www.quanshuwang.com/book/9/9055
#获取主页面源代码
# headers={
#     'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
#  }
#定义方法
def getNovelContent():   #type(html)-->bytes类型转成字符串
    html=urllib.request.urlopen('http://www.quanshuwang.com/book/9/9055').read()    #获取网页源代码
    # print(html.status)   #状态码200-->成功访问
    #解码
    html=html.decode("gbk")
    # print(html)    #正常显示中文
#获取章节超链接
    #<li><a href="http://www.quanshuwang.com/book/9/9055/9674284.html" title="第二十一章 地下河，共3568字">第二十一章 地下河</a></li>
    #正则表达式获取章节   匹配所有章节  匹配所有，分组匹配
    req='<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    urls=re.findall(req,html)
    # print(urls)
    for i in urls:
        # print(i)       #输出-->网址加标题
        novel_url=i[0]   #索引  -->章节url
        novel_name=i[1]     #章节标题
        # print(novel_url)
        # print(novel_name)
        chapt=urllib.request.urlopen(novel_url).read()
        chapt_html=chapt.decode("gbk")
        # print(chapt_html)
#获取小说内容
        reg='</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'   #提取头和尾
        #多行匹配
        reg=re.compile(reg,re.S)
        chapt_content=re.findall(reg,chapt_html)
        # print(chapt_content[0])    #爬爬爬  将列表变成字符串
        #将页面标签去掉    #将<br />\r\n<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;替换成空格
        chapt_content=chapt_content[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
        chapt_content=chapt_content.replace("<br />","")
        # print(chapt_content)
        # exit   一章
        print("正在下载:"+novel_name)
        #字符串格式化      #无数据格式    w---->读写模式   wb-->二进制读写
        # f=open('{}.doc'.format(novel_name),'w')
        # f.write(chapt_content)
        with open('{}.doc'.format(novel_name),'w')as f:
            f.write(chapt_content)

getNovelContent()