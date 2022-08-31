import requests
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def download(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
               ' Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}

    response = requests.get(url,headers=headers)

    html = etree.HTML(response.text)
    lis = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')

    for it in lis:
        price = it.xpath('./div/div[2]/strong/i/text()')
        name = it.xpath('./div/div[3]/a/i/text()')
        shop = it.xpath('./div/div[5]/span/a/text()')

        print(price,name,shop)


if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:

        for itt in range(1,11,2):
            t.submit(download,f'https://search.jd.com/Search?keyword=%E5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%B'
                              f'Fprimeb660&pvid=0d98c370a6ed48728a41338c06d83295&page={itt}&s=61&click=0')


            #download(f'https://search.jd.com/Search?keyword=%E5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%BFprimeb660&pvid=0d98c370a6ed48728a41338c06d83295&page={3}&s=61&click=0')


