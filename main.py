import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://sinoptik.ua/pohoda/dolyna')
        soup = BeautifulSoup(html, "html.parser")
        first_day = soup.find(class_="+Ncy59Ya")
        first_day_p = first_day.find_all('p')
        for p in reversed(first_day_p):
            print(p.get_text())
            break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())