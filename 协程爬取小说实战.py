import asyncio
import aiofiles
import requests
import aiohttp
from lxml import etree
from bs4 import BeautifulSoup

main_url = 'https://www.biquge.biz/'
url = 'https://www.biquge.biz/22_22780/'

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await etree.HTML(response.text())
            title = await html.xpath('/html/body/div/div[5]/div/div[2]/h1/text()')
            content = await html.xpath('/html/body/div/div[5]/div/div[3]/text()')

            async with aiofiles.open('小说/'+title,'w') as file:
                await file.write(f'{title}\n')
                await file.write(f'{content}\n')



async def main(url):

    response = requests.get(url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    dds = html.xpath('/html/body/div/div[6]/div/dl/dd')

    task = []

    for it in dds:
        href = it.xpath('./a/@href')[0]
        child_href = main_url+href

        asyncio_creat = asyncio.create_task(download(child_href))
        task.append(asyncio_creat)

    await asyncio.wait(task)

if __name__ == '__main__':
    #url = 'https://www.biquge.biz/22_22780/'
    asyncio.run(main(url))





