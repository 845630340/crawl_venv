import requests
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime


home_url = 'https://pacaio.match.qq.com/irs/rcd?cid=4&token=9513f1a78a663e1d25b46a826f248c3c&ext=&page=0'
r = requests.get(home_url, headers=headers)
print(r.status_code)
all_datas = []
json_data = r.json().get('data', None)
if json_data is None:
    print('no data!')
else:
    for item in json_data:
        data = {}
        data['title'] = item['title']
        data['abstract'] = item['intro']
        data['comments_count'] = item['view_count']
        data['release_time'] = item['publish_time']  # str(now) -> datetime(need)
        data['chinese_tag'] = item['category_chn']
        data['label'] = [x[0] for x in item['tag_label']]
        data['source_url'] = item['vurl']
        all_datas.append(data)

for i in all_datas:
    print(i)
