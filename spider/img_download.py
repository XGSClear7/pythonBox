import asyncio
import csv
import os
import re

import aiohttp

IMG_PATH = r'F:\资料\Fuze'


async def img_download(session, url):
    # 处理url
    url = url[0].split('?')[0]
    img_name = re.findall('airfilterlocation/(.*)', url)[0].replace('/', '-')
    img_path = os.path.join(IMG_PATH, img_name)
    if not os.path.exists(img_path):
        print(f'正在下载。。。{img_name}')
        img = await session.get(url)
        imgcode = await img.read()
        with open(img_path, 'wb') as f:
            f.write(imgcode)
    print(f'已经存在。。。{img_name}')
    return img_name


async def main(loop, URL):
    # 建立会话
    async with aiohttp.ClientSession() as session:
        # 创建任务
        tasks = [loop.create_task(img_download(session, url)) for url in URL]
        # 等待任务完成
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [i.result() for i in finished]
        print(all_results)


if __name__ == '__main__':
    print('正在读取URL列表。。。')
    URLData = [i for i in csv.reader(
        open(r'F:\MyProjects\ZhipeiAppSpider\data\FuzeBox_img.csv', 'r', encoding='utf-8-sig'))]
    print('开始任务。。。')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, URLData))
    print('图片下载完成')
