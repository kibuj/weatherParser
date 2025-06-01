import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(link):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, link)
        soup = BeautifulSoup(html, "html.parser")
        def temp():
            temp = soup.find_all(class_="+Ncy59Ya")
            first_day = []
            for i in temp:
                first_day.append(i.get_text())
                if len(first_day) == 2:
                    break
            print(first_day)
        temp()


loop = asyncio.get_event_loop()
loop.run_until_complete(main('https://sinoptik.ua/pohoda/dolyna'))
loop.run_until_complete(main('https://sinoptik.ua/pohoda/moskva'))
