import requests
import aiohttp
import aiofiles
import asyncio
from lxml import etree
from bs4 import BeautifulSoup
import re

main_url = 'http://www.mianfeixiaoshuoyueduwang.com/'
url = 'http://www.mianfeixiaoshuoyueduwang.com/book/1106/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}

response = requests.get(url,headers=headers)
html = etree.HTML(response.text)
lis = html.xpath('/html/body/div[3]/div[4]/ul/li')

list1 = []

for it in lis:
    href = it.xpath('./a/@href')[0]
    child_href = main_url+href
    list1.append(child_href)
    #print(child_href)

async def download(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            response_text = await response.text()

            page = BeautifulSoup(response_text,'html.parser')
            title = page.find('h1',class_="title1").text
            content = page.find_all('p')

            async with aiofiles.open('小说1/'+title,'w') as file:
                await file.write(f'{title}\n')

            async with aiofiles.open('小说1/'+title,'a') as file1:

                for itt in content:
                    itt = str(itt)
                    line = itt.strip('<p>').strip('</p>')
                    await file1.write(f'\t{line}')
                #print(content)

async def main():
    tasks = []

    for ittt in list1:
        task = download(ittt)
        task_object = asyncio.create_task(task)
        tasks.append(task_object)

    await asyncio.wait(tasks)


if __name__ == '__main__':

    asyncio.run(main())
