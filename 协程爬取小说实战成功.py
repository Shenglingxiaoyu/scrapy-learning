import requests
import aiohttp
import asyncio
import aiofiles
from lxml import etree

main_url = 'https://www.17k.com'
url = 'https://www.17k.com/list/1398783.html'

async def download(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            html = etree.HTML(response_text)

            title = html.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/h1/text()')[0]
            content = html.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/p/text()')
            content = ''.join(content)

            async with aiofiles.open('小说/'+title,'w') as file:
                await file.write(f'{title}\n'+f'{content}')

async def main(url):

    response = requests.get(url)
    html = etree.HTML(response.text)
    aas = html.xpath('/html/body/div[5]/dl[2]/dd/a')[:90]

    tasks = []

    for it in aas:
        href = it.xpath('./@href')[0]
        child_hrefs = main_url+href

        task = asyncio.create_task(download(child_hrefs))
        tasks.append(task)

    await asyncio.wait(tasks)

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(url))
