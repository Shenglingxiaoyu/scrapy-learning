import requests
from lxml import etree

url = 'https://www.mcbbs.net/forum-mod-1.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

response = requests.get(url,headers=headers)
html = etree.HTML(response.text)

result = html.xpath('/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div[5]/div[2]/form/table/tbody')[12:]

for it in result:
    name = it.xpath('./tr/th/a[3]/text()')
    print(name[0])


#print(response.text)