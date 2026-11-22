import asyncio
from playwright.async_api import async_playwright
PORT=int(open('.port').read())
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=await b.new_page(viewport={'width':1920,'height':1080})
    await pg.goto(f'http://127.0.0.1:{PORT}/index.html#1',wait_until='networkidle'); await pg.evaluate('document.fonts.ready')
    await pg.emulate_media(media='print')
    await pg.pdf(path='out/unesr-dict-adonay-lizardo.pdf',width='1920px',height='1080px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
    await b.close()
asyncio.run(main())
