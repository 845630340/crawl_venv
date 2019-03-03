import requests
import time
import random
from datetime, timedelta
from crawl_venv.crawl_data_to_mongo.mongo.operation import TencentOperation


class TencentCrawl:
    headers = {
        "referer": "https://news.qq.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "cookie": """pgv_info=ssid=s498267480; pgv_pvid=7865358422; pgv_pvi=9306355712; pgv_si=s2089503744; pac_uid=0_5c7b64d04640c"""
    }

    def get_data(self, n):
        tencentOP = TencentOperation()
        urls = [
            'https://pacaio.match.qq.com/irs/rcd?cid=108&ext=&token=349ee24cdf9327a050ddad8c166bd3e3&page={}',
            'https://pacaio.match.qq.com/irs/rcd?cid=4&token=9513f1a78a663e1d25b46a826f248c3c&ext=&page={}',
        ]
        for url in urls:
            i = 0
            while True:
                print('index is :',i+1)
                url = url.format(i)
                r = requests.get(url, headers=self.headers)
                json_data = r.json().get('data', None)
                if json_data is None:
                    break
                else:
                    all_datas = []
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
