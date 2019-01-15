# -*- coding:utf8 -*-

import requests
import random
import time
from datetime import datetime
from lxml import etree
from crawl_data_to_mongo.mongo.operation import ObserverOperation


class ObserverCrawl:

    def strtime_to_datetime(self, str_time):
        release_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        return release_time

    def get_data(self, n):
        observerOP = ObserverOperation()
        s = requests.Session()

        for i in range(1, n+1):
            all_datas = []
            url = 'https://www.guancha.cn/mainnews-yw/list_{}.shtml'.format(i)
            r = s.get(url)
            r.encoding = "UTF-8"
            if r is None or r.status_code != 200:
                raise Exception('Request Error!')
            base_data = etree.HTML(r.text)
            for i in range(1, 21):
                data = {}
                data['title'] = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/h4/a/text()'.format(i))[0]
                data['abstract'] = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/p/text()'.format(i))[0]
                data['comments_count'] = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/div/a[1]/text()'.format(i))[0]
                str_release_time = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/div/span/text()'.format(i))[0]
                data['release_time'] = self.strtime_to_datetime(str_release_time)
                source_url_part = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/a/@href'.format(i))[0]
                data['source_url'] = 'https://www.guancha.cn' + source_url_part
                data['chinese_tag'] = source_url_part.split('/')[1]
                all_datas.append(data)
            observerOP.save_all_datas(all_datas)
            time.sleep(random.randint(3, 10))


observer = ObserverCrawl()
observer.get_data(2)

