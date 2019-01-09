# -*- coding:utf8 -*-
import requests
import time
#from crawl_data_to_mongo.mongo.operation import TouTiaoOperation

class ToutiaoCrawl:
    name = 'Toutiao'
    def display(self, a_dict):
        data_list = a_dict['data']
        next_time = a_dict['next']['max_behot_time']
        for each_dict in data_list:
            if 'chinese_tag' in each_dict:
                for k, v in each_dict.items():
                    print k, '---', v
                print '--------------'
        print '----------------------'
        print 'next_time :', next_time

    def get_data(self):
        #toutiaoOP = TouTiaoOperation()

        #home_url = 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0'
        home_url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time=1546944588'
        headers = {
            "accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://www.toutiao.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

        all_datas = []
        r = requests.get(home_url, headers=headers)
        self.display(r.json())
        '''
        json_data = r.json()['data']
        next_time = r.json()['next']['max_behot_time']
        #home_url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time={}'.format(str(next_time))
        print 'next_time is :', next_time
        for each_dict in json_data:
            if 'chinese_tag' in each_dict:
                data = {}
                data['title'] = each_dict['title']
                data['abstract'] = each_dict['abstract']
                data['chinese_tag'] = each_dict['chinese_tag']
                data['comments_count'] = each_dict['comments_count']
                data['label'] = each_dict['label']
                data['source_url'] = each_dict['source_url']
                all_datas.append(data)
        toutiaoOP.save_all_datas(all_datas)'''

toutiao = ToutiaoCrawl()
toutiao.get_data()