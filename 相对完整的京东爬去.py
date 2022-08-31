import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%BF' \
      'b660&enc=utf-8&wq=%E5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%BFb660&pvid=9d2ed00d63e74c09a9c4e309f54a6482'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}

response = requests.get(url,headers=headers)
html = etree.HTML(response.text)
lis = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')

for it in lis:
    name = it.xpath('./div/div[3]/a/em/text()')
    price = it.xpath('./div/div[2]/strong/i/text()')
    name1 = ','.join(name)
    price1 = ''.join(price)

    #print(name1,price1)
    with open('京东1','a') as file:
        file.write(price1)
        file.write(f'{name1}\n')

