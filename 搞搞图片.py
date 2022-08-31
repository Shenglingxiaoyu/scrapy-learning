import requests
from bs4 import BeautifulSoup
url1 = 'https://pic.netbian.com/'
url = 'https://pic.netbian.com/4kdongman/'

response = requests.get(url)
response.encoding = 'gbk'
#print(response.text)

main_page = BeautifulSoup(response.text,'html.parser')             #注意beautiful解析只有find和find_all两个
ullist1 = main_page.find("ul",class_="clearfix").find_all("a")

#print(ullist1)                             beautiful可以拿到标签意外的值，get可以拿到标签以内的值
for a in ullist1:                    #迭代器，for in 循环，有第一才有第二，第一和第二不能同时存在，第一结束后留下去到第二
    href = a.get('href')
    child_href = url1+href.strip('/')     #单独在最前面提取出来，数据就只有第一组，之后在for in循环中才会留到第二个

    child_href_response = requests.get(child_href,'html=parser')     #想要序列找东西，需要在循环的后面写，不能超过循环
    child_href_response.encoding ='gbk'

    child_page = BeautifulSoup(child_href_response.text)
    ullist2 = child_page.find("div",class_="photo-pic")

    img = ullist2.find("img")
    scr = img.get('src')
    img_response = requests.get(scr)




