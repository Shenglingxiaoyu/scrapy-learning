import requests
from bs4 import BeautifulSoup

url = 'https://www.mcbbs.net/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

response = requests.get(url,headers=headers)

html = BeautifulSoup(response.text,'html.parser')
result = html.find('div',id="slideshow_3").find_all('div',class_='image')

list = []

for it in result:
    a = it.find('a')
    child_download = a.get('href').strip('/')

    main_child_download = url+child_download
    print(main_child_download)

    img = a.find('img')
    name = img.get('alt')
    print(name)


