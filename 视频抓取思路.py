import requests
import aiohttp
import asyncio
import aiofiles
from lxml import etree
from bs4 import BeautifulSoup
import re

main_url = 'https://www.imomoedm.com'
url = 'https://www.imomoedm.com/dmdetail/shicaolaolongbeiguanyielongzhiming.html-1-1.html'
list1 = []
list3 = []

def child_url(url):

    response = requests.get(url)
    html = etree.HTML(response.text)
    lis = html.xpath('/html/body/div[2]/div[7]/div[2]/div[2]/ul/div/ul/li')

    for it in lis:
        href = it.xpath('./a/@href')[0]
        child_url = main_url+href
        list1.append(child_url)

def video_url(url):

    obj = re.compile(r'"},"url":"(?P<video_url>.*?)"')
    response = requests.get(url)
    video_url = obj.search(response.text).group('video_url').replace('\\','')

    return video_url

def m3u8_url(url):

    m3u8_domain = 'https://s7.fsvod1.com'

    obj = re.compile(r'"url":"(?P<m3u8>.*?)"')
    response = requests.get(url)
    m3u8 = obj.search(response.text).group('m3u8')
    m3u8_url = m3u8_domain+m3u8

    return  m3u8_url

def m3u8_text(url):

    response = requests.get(url)
    with open('video/m3u8','w') as file:
        file.write(response.text)

def ts_url():

    ts_domain = 'https://s7.fsvod1.com'
    with open('video/m3u8','r') as file:
        for it in file:
            if it.startswith('#'):
                continue
            else:
                it = it.strip('\n')
                ts_url = ts_domain+it
                list3.append(ts_url)

async def download(url,name,session):

    async with session.get(url) as response:
        response_content = await response.content.read()
        async with aiofiles.open(f'video/{name}','wb') as file:
            await file.write(response_content)
    print(f'{name}下载完成')

async def main():

    tasks = []

    async with aiohttp.ClientSession() as session:
        for it in list3:
            name = it.split('/')[-1]
            task = download(it,name,session)
            task_object = asyncio.create_task(task)
            tasks.append(task_object)

        await asyncio.wait(tasks)

if __name__ == '__main__':

    list2 = []
    child_url(url)

    for it in list1:
        video_url = video_url(it)
        print(video_url)

    for itt in list2:
        m3u8_url = m3u8_url(itt)
        print(m3u8_url)

    ts_url()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
