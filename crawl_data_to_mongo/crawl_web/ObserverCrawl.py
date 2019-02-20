
import requests
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree
from crawl_venv.crawl_data_to_mongo.mongo.operation import ObserverOperation


class ObserverCrawl:
    """
    Info: the content of chinese_tag is English.
    """

    def get_label(self, source_url):
        label_list = []
        r = requests.get(source_url)
        r.encoding = "UTF-8"
        base_data = BeautifulSoup(r.text, 'lxml')
        label = base_data.find('div', class_="key-word").select('span')
        for keyword in label[1:]:
            label_list.append(keyword.text)
        return label_list

    def strtime_to_datetime(self, str_time):
        release_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        return release_time

    def get_data(self, n):
        observerOP = ObserverOperation()
        s = requests.Session()

        for i in range(1, n + 1):
            print('index is :', i)
            all_datas = []
            url = 'https://www.guancha.cn/mainnews-yw/list_{}.shtml'.format(i)
            r = s.get(url)
            r.encoding = "UTF-8"
            if r is None or r.status_code != 200:
                raise Exception('Request Error!')
            base_data = etree.HTML(r.text)
            for i in range(1, 21):
                try:
                    data = {}
                    data['title'] = \
                    base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/h4/a/text()'.format(i))[0]
                    data['abstract'] = \
                    base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/p/text()'.format(i))[0]
                    data['comments_count'] = \
                    base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/div/a[1]/text()'.format(i))[0]
                    str_release_time = \
                    base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/div/div/span/text()'.format(i))[0]
                    data['release_time'] = self.strtime_to_datetime(str_release_time)
                    source_url_part = base_data.xpath('/html/body/div[2]/div[3]/ul/li[1]/ul/li[{}]/a/@href'.format(i))[0]
                    source_url = 'https://www.guancha.cn' + source_url_part
                    data['source_url'] = source_url
                    data['chinese_tag'] = source_url_part.split('/')[1]
                    data['label'] = self.get_label(source_url)
                    all_datas.append(data)
                except:
                    continue
            observerOP.update_all_datas(all_datas)
            time.sleep(random.randint(2, 5))


observer = ObserverCrawl()
observer.get_data(15)  # max value of param is 15, suggest to look at the web page
