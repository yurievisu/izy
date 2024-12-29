import asyncio
import aiohttp
import re
from rich.console import Console
import sys
import os

os.system('clear')
console = Console()
config = {
    'cookies': '',
    'post': ''
}

def banner():
    console.print("""
 __     ______     __  __    
/\ \   /\___  \   /\ \_\ \   
\ \ \  \/_/  /__  \ \____ \  
 \ \_\   /\_____\  \/\_____\ 
  \/_/   \/_____/   \/_____/ 
                             
    """, style="blue")

banner()
config['cookies'] = input("\033[0mCOOKIE : \033[92m")
config['post'] = input("\033[0mPOST LINK : \033[92m")
share_count = int(input("\033[0mSHARE COUNT : \033[92m"))

if not config['post'].startswith('https://'):
    console.print("Invalid post link", style="red")
    sys.exit()
elif not share_count:
    console.print("Share count cannot be zero", style="red")
    sys.exit()

os.system("clear")
banner()

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': "Android",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}

class Share:
    async def get_token(self, session):
        headers['cookie'] = config['cookies']
        async with session.get('https://business.facebook.com/content_management', headers=headers) as response:
            data = await response.text()
            access_token = 'EAAG' + re.search('EAAG(.*?)","', data).group(1)
            return access_token, headers['cookie']

    async def share(self, session, token, cookie):
        headers['cookie'] = cookie
        headers['accept-encoding'] = 'gzip, deflate'
        headers['host'] = 'b-graph.facebook.com'
        
        count = 1
        with console.status("[bold green]Sharing posts...") as status:
            while count < share_count + 1:
                async with session.post(
                    f'https://b-graph.facebook.com/me/feed?link=https://mbasic.facebook.com/{config["post"]}&published=0&access_token={token}',
                    headers=headers
                ) as response:
                    data = await response.json()
                    if 'id' in data:
                        console.log(f"Share {count}/{share_count} completed")
                        count += 1
                    else:
                        console.log("[bold red]Cookie is blocked or invalid!")
                        console.log(f"[white]Total successful shares: [bold green]{count-1}")
                        break

async def main(num_tasks):
    async with aiohttp.ClientSession() as session:
        share = Share()
        token, cookie = await share.get_token(session)
        tasks = []
        for i in range(num_tasks):
            task = asyncio.create_task(share.share(session, token, cookie))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main(1))
