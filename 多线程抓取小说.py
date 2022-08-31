import requests
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

main_url = 'https://www.17k.com'
url = 'https://www.17k.com/list/2498066.html'

response = requests.get(url)
response.encoding = 'utf-8'

html = etree.HTML(response.text)
ass = html.xpath('/html/body/div[5]/dl[2]/dd/a')

list1 = []

for it in ass:
    href = it.xpath('./@href')[0]

    hrefs = main_url+href
    list1.append(hrefs)

    # print(hrefs)
list1 = list1[:46]

def download(url):

    child_response = requests.get(url)
    child_response.encoding = 'utf-8'

    html = etree.HTML(child_response.text)
    title = html.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/h1/text()')[0]
    content = html.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/p/text()')

    content = ''.join(content)

    with open('book','a') as file:
        file.write(title)
        file.write(f'{content}\n')
    #print(title,content)

with ThreadPoolExecutor(10) as t:

    for itt in list1:
        t.submit(download,itt)
        #download('https://www.17k.com/chapter/2498066/28684773.html')

#print(list1)
#print(response.text)