import asyncio,glob
from playwright.async_api import async_playwright
from PIL import Image
PORT=int(open('.port').read())
SIZES=[(1920,1080,1),(1366,768,1),(1440,600,1),(390,844,2)]
async def main():
  errs=[]
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for w,h,dpr in SIZES:
      ctx=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr)
      pg=await ctx.new_page()
      pg.on('console',lambda m:errs.append(f'{w}x{h} console {m.type}: {m.text}') if m.type in('error','warning') else None)
      pg.on('pageerror',lambda e:errs.append(f'{w}x{h} pageerror {e}'))
      pg.on('requestfailed',lambda r:errs.append(f'{w}x{h} reqfailed {r.url}'))
      pg.on('response',lambda r:errs.append(f'{w}x{h} http {r.status} {r.url}') if r.status>=400 else None)
      pg.on('request',lambda r:errs.append(f'{w}x{h} EXTERNAL {r.url}') if not r.url.startswith(f'http://127.0.0.1:{PORT}') and not r.url.startswith('data:') else None)
      await pg.goto(f'http://127.0.0.1:{PORT}/index.html#1',wait_until='networkidle'); await pg.evaluate('document.fonts.ready')
      n=await pg.evaluate('window.__deck.N')
      for i in range(n):
        await pg.evaluate(f'window.__deck.go({i})'); await pg.wait_for_timeout(250)
        await pg.screenshot(path=f'shots/{w}x{h}/slide-{i+1}.png')
      await ctx.close()
    await b.close()
  print('ERRORS:',len(errs)); print('\n'.join(errs))
  def sheet(folder,out,cols,tw):
    fs=sorted(glob.glob(f'shots/{folder}/slide-*.png')); im0=Image.open(fs[0]); th=int(tw*im0.height/im0.width); pad=16
    rows=(len(fs)+cols-1)//cols
    S=Image.new('RGB',(cols*(tw+pad)+pad,rows*(th+pad)+pad),(40,40,40))
    for k,f in enumerate(fs):
      S.paste(Image.open(f).convert('RGB').resize((tw,th),Image.LANCZOS),(pad+(k%cols)*(tw+pad),pad+(k//cols)*(th+pad)))
    S.save(out)
  sheet('1920x1080','shots/contact-sheet.png',2,960)
  sheet('390x844','shots/contact-sheet-phone.png',4,390)
asyncio.run(main())
