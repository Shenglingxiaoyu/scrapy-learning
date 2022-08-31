import requests
import asyncio
import aiohttp
import aiofiles
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://b.faloo.com/html_1114_1114146/'
response = requests.get(url)

html = etree.HTML(response.text)
href = html.xpath('/html/body/div[2]/div[3]/div[4]/div[3]/a/@href')

child_url = ['https:'+it for it in href]

async def download(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            response_text = await response.text(encoding='GB18030')
            page = BeautifulSoup(response_text,'html.parser')
            title = page.find('h1').text
            content = page.find_all('p')[:-9]
            content = [str(itt).strip('<p>“').strip('”</p>') for itt in content]
            content = ''.join(content)

            async with aiofiles.open(f'video/{title}','w') as file:
                await file.write(f'{title}\n'+f'\t{content}')
async def main():
    tasks = []

    for it in child_url:
        task = download(it)
        task_object = asyncio.create_task(task)
        tasks.append(task_object)

    await asyncio.wait(tasks)

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
