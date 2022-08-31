import requests
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

main_url = 'https://www.biquge.biz/'
url = 'https://www.biquge.biz/0_32/'

response = requests.get(url)
html = etree.HTML(response.text)
dds = html.xpath('/html/body/div/div[6]/div/dl/dd')

list1 = []

for it in dds:
    href = it.xpath('./a/@href')[0]
    child_href = main_url+href
    list1.append(child_href)

    #print(child_href)

def download(url):

    child_response = requests.get(url)
    child_html = etree.HTML(child_response.text)
    title = child_html.xpath('/html/body/div/div[5]/div/div[2]/h1/text()')
    content = child_html.xpath('/html/body/div/div[5]/div/div[3]/text()')
    final = ''.join(content)


    print(title,final)


if __name__ == '__main__':

    with ThreadPoolExecutor(5) as t:
        for itt in list1:
            t.submit(download,itt)     #在提交任务的时候，传参要用逗号

'''好处是速度快，但抓取不是按顺序来'''

