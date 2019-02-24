import requests
import time
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from crawl_venv.crawl_data_to_mongo.mongo.operation import TouTiaoOperation


class ToutiaoCrawl:
    """
    1. Fields: title, abstract, chinese_tag, comments_count, label, source_url, date (the crawl datetime)
    2. Be careful: maybe need to change the cookie every time you crawl, otherwise the request will be wrong.
    """
    # headers = {
    #     "accept": "text/javascript, text/html, application/xml, text/xml, */*",
    #     "content-type": "application/x-www-form-urlencoded",
    #     "referer": "https://www.toutiao.com/",
    #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    #     "cookie": """tt_webid=6642930114115356168; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1681d2ce83d562-0ee42d42f41f97-10336653-13c680-1681d2ce83edb4; tt_webid=6642930114115356168; csrftoken=7dd3951af35b50bf3d31720879f7995a; uuid="w:5d95a3d5775e407b8ab2617da925d965"; CNZZDATA1259612802=491698772-1546675650-https%253A%252F%252Fwww.google.com%252F%7C1547193903; __tasessionId=8uun05bwi1547195138926"""
    # }
    headers = {
        "accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "content-type": "application/x-www-form-urlencoded",
        "referer": "https://www.toutiao.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "cookie": """tt_webid=6655643402406102536; UM_distinctid=168f4dc1efd563-0edd3884fce288-47e1039-100200-168f4dc1efe1c; csrftoken=998e2804c04c8bcf3de3a1a7ef61484e; __tasessionId=5oii3qns51550802050625; tt_webid=6655643402406102536; WEATHER_CITY=%E5%8C%97%E4%BA%AC; CNZZDATA1259612802=1311904284-1550291036-%7C1550800180"""
    }

    def display(self, a_dict):
        """
        :param a_dict: response.json()
        :return: to show the json data in the IDE screen
        action: Just for testing purposes
        """
        data_list = a_dict['data']
        next_time = a_dict['next']['max_behot_time']
        for each_dict in data_list:
            if 'chinese_tag' in each_dict:
                for k, v in each_dict.items():
                    print(k, '---', v)
                print('--------------')
        print('----------------------')

    def get_release_time(self, source_url):
        """
        Enter source_url page to crawl release_time.
        Maybe can filter many url, beceuse of the different format of web page.
        Highly unstable，make do with it!
        """
        try:
            r = requests.get(source_url, headers=self.headers, timeout=3).text
            base_data = BeautifulSoup(r, 'lxml')

            date = ''
            date_list = base_data.find_all('script')[:]
            for each in date_list:
                if 'time' in each.text:
                    date = each.text
            index = date.index('time')
            str_time = date[index + 7:index + 26]
            release_time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
            return release_time
        except:
            return None

    def get_data(self, n):
        toutiaoOP = TouTiaoOperation()
        home_url = 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0'
        #home_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&max_behot_time=0'
        for i in range(n):
            print('index is :', i + 1)
            all_datas = []
            r = requests.get(home_url, headers=self.headers)

            json_data = r.json().get('data', None)
            if json_data is None:
                raise StopIteration('Finish : TouTiao crawl to the buttom')

            next_time = r.json()['next']['max_behot_time']
            home_url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time={}'.format(str(next_time))

            for each_dict in json_data:
                if 'chinese_tag' in each_dict and 'comments_count' in each_dict and 'label' in each_dict and \
                        'abstract' in each_dict and 'source_url' in each_dict and 'behot_time' in each_dict:
                    data = {}
                    source_url = 'https://www.toutiao.com' + each_dict['source_url']
                    release_time = self.get_release_time(source_url)
                    if release_time:
                        data['release_time'] = release_time
                    else:
                        data['release_time'] = datetime.now() - timedelta(hours=1)
                    data['title'] = each_dict['title']
                    data['abstract'] = each_dict['abstract']
                    data['chinese_tag'] = each_dict['chinese_tag']
                    data['comments_count'] = each_dict['comments_count']
                    data['label'] = each_dict['label']
                    data['source_url'] = source_url
                    all_datas.append(data)
            toutiaoOP.update_all_datas(all_datas)
            time.sleep(random.randint(4, 7))


toutiao = ToutiaoCrawl()
toutiao.get_data(300)  # seems to be no limit to the number of TouTiao's requests
