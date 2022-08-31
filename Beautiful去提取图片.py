import requests
from bs4 import BeautifulSoup

url = "https://pic.netbian.com/"
response = requests.get(url)
response.encoding = 'gbk'

response.close()
#print(response.text)

main_page = BeautifulSoup(response.text,'html.parser')
ul = main_page.find('ul',class_="clearfix")
result = ul.find_all('a')

for it in result:
    href = it.get('href')
    child_href = url+href.strip('/')

    child_response = requests.get(child_href)
    child_response.encoding = 'gbk'

    child_response.close()

    child_page = BeautifulSoup(child_response.text,'html.parser')
    child_title = child_page.find('div',class_="photo-pic")

    img = child_title.find('img')
    src = img.get("src")
    picture_ulr = url+src.strip('/')
    print(picture_ulr)