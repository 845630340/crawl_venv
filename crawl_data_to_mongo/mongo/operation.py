# -*- coding:utf8 -*-

import logging
from model import TouTiaoModel
from datetime import datetime
from mongoengine import connect

logging.basicConfig(level=logging.DEBUG)


class TouTiaoOperation:
    def __init__(self):
        connect('db_web_data')
        logging.info('connect mongo successfully!')

    def save_data(self, data):
        """
        behot_time: datetime.datetime -> str
        create_time: datetime.datetime -> str
        time_span: datetime.timedelta
        """
        create_date = datetime.now()
        toutiao = TouTiaoModel(
            title=data['title'],
            abstract=data['abstract'],
            chinese_tag=data['chinese_tag'],
            comments_count=data['comments_count'],
            label=data['label'],
            source_url=data['source_url'],
            release_time=data['release_time'].strftime('%Y-%m-%d %H:%M:%S'),
            crawl_time=create_date.strftime('%Y-%m-%d %H:%M:%S'),
            time_span=str(create_date - data['release_time'])
        )
        try:
            toutiao.save()
            logging.info('toutiao save one data successfully.')
        except Exception, e:
            logging.info('toutiao failed to save one data | error : {}'.format(e))

    def save_all_datas(self, datas):
        for data in datas:
            self.save_data(data)
        logging.info('---toutiao save ALL datas successfully---')

    def get_data(self):
        model = TouTiaoModel
        data = model.objects.no_cache()
        return data
