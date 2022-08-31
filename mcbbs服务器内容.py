import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://www.mcbbs.net/forum-server-1.html'
main_url = 'https://www.mcbbs.net/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

response = requests.get(url,headers=headers)
html = etree.HTML(response.text)
tbodys = html.xpath('/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div[6]/div[3]/form/table/tbody')[2:]

list = []
list1 = []

for it in tbodys:
    href = it.xpath('./tr/th/a[3]/@href')[0]
    child_connect = main_url+href

    child_response = requests.get(child_connect,headers=headers)
    child_page = BeautifulSoup(child_response.text,'html.parser')

    div = child_page.find('div',class_="typeoption").find_all('tr')

    for itt in div:
        name = itt.find('td')
        print(name.text)