import requests
from bs4 import BeautifulSoup

url = 'https://music.douban.com/chart'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

response = requests.get(url,headers=headers)
response.close()

mian_page = BeautifulSoup(response.text,'html.parser')

ul = mian_page.find('ul',class_="col5")
lis = ul.find_all('li')                          #find_all的结果是列表，想要继续下面就要将列表遍历

for it in lis:
    download = it.find('a',class_="face")

    name = it.find('p')
    print(download.get('href'),name)