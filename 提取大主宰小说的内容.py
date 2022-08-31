import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://www.biquge.biz/0_32/'
main_url = 'https://www.biquge.biz/'
response = requests.get(url)
response.close()

html = etree.HTML(response.text)
dds = html.xpath('/html/body/div/div[6]/div/dl/dd')

list = []
list1 = []

for it in dds:
    href = it.xpath('./a/@href')[0]
    child_connect = main_url+href
    list.append(child_connect)
    #print(child_connect)

for itt in list:
    child_response = requests.get(itt)
    child_html = etree.HTML(child_response.text)
    name = child_html.xpath('/html/body/div/div[5]/div/div[2]/h1/text()')
    content = child_html.xpath('/html/body/div/div[5]/div/div[3]/text()')
    result = ''.join(content)
    #content.strip('\u3000\u3000')

    print(name,result)

#print(response.text)