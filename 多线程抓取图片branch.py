import requests
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

main_url = 'https://pic.netbian.com'
url1 = 'https://pic.netbian.com/4kdongman/index.html'



def download(url):
    response = requests.get(url)
    response.encoding = 'gbk'

    html = etree.HTML(response.text)
    lis = html.xpath('/html/body/div[2]/div/div[3]/ul/li')

    list1 = []
    list2 = []

    for it in lis:
        href = it.xpath('./a/@href')[0]
        child_hrefs = main_url+href
        list1.append(child_hrefs)

    for itt in list1:

        child_response = requests.get(itt)
        child_response.encoding = 'gbk'

        html1 = BeautifulSoup(child_response.text,'html.parser')
        pics = html1.find('div',class_="photo-pic")
        img = pics.find('img')
        srcs = img.get('src')

        child_src = main_url+srcs

        list2.append(child_src)

    for ittt in list2:

        final_response = requests.get(ittt)
        final_response.encoding = 'gbk'

        name = ittt.split('/')[-1]

        with open('jpg/'+name,'ab') as file:
            file.write(final_response.content)

    del list1
    del list2







if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:
        for itttt in range(2,25):
            t.submit(download,f'https://pic.netbian.com/4kdongman/index_{itttt}.html')

