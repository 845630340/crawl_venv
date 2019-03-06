import requests
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

headers = {
    "referer": "https://news.qq.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "cookie": """pgv_info=ssid=s498267480; pgv_pvid=7865358422; pgv_pvi=9306355712; pgv_si=s2089503744; pac_uid=0_5c7b64d04640c"""
}
i = 0
while True:
    print('index is:', i)
    home_url = 'https://pacaio.match.qq.com/irs/rcd?cid=108&ext=&token=349ee24cdf9327a050ddad8c166bd3e3&page={}'.format(i)
    r = requests.get(home_url, headers=headers)

    all_datas = []
    json_data = r.json().get('data', None)
    if not json_data:
        print('no data!')
        break
    else:
        for item in json_data:
            data = {}
            data['title'] = item['title']
            # data['abstract'] = item['intro']
            # data['comments_count'] = item['view_count']
            # data['release_time'] = item['publish_time']  # str(now) -> datetime(need)
            # data['chinese_tag'] = item['category_chn']
            # data['label'] = [x[0] for x in item['tag_label']]
            # data['source_url'] = item['vurl']
            all_datas.append(data)
        for j in all_datas:
            print(j['title'])
        print('---------------------------------------------')

        i += 1
