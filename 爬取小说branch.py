import requests
import asyncio
import aiofiles
import aiohttp
from lxml import etree
from bs4 import BeautifulSoup

main_url = 'https://www.1qxs.com'
url = 'https://www.1qxs.com/list/33101.html'
response = requests.get(url)
html = etree.HTML(response.text)
hrefs = html.xpath('/html/body/div[3]/div[3]/div/ul/ul/li/a/@href')
child_url = [main_url+it for it in hrefs]

async def download(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            response_text = await response.text(encoding='utf-8')
            html = etree.HTML(response_text)
            title = html.xpath('/html/body/div[4]/div/div[1]/div[2]/h1/text()')[0]
            title = title.split('(')[0]
            content = html.xpath('/html/body/div[4]/div/div[1]/div[3]/p/text()')[1:]

            async with aiofiles.open('video1'+title,'a',encoding='GB18030') as file:

                await file.writelines(content)

    print('over')

async def main():
    tasks = []

    for it in child_url:
        task = download(it)
        task_object = asyncio.create_task(task)
        tasks.append(task_object)
        tasks.append(task_object)

    await asyncio.wait(tasks)

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
