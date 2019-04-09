# -*- coding:utf8 -*-

import logging
from .model import TouTiaoModel, ObserverModel, TencentModel
from datetime import datetime
from mongoengine import connect

logging.basicConfig(level=logging.DEBUG)


class TouTiaoOperation:
    def __init__(self):
        connect('db_web_data')
        logging.info('connect mongo: TouTiao successfully!')

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
        except Exception as e:
            logging.info('toutiao failed to save one data | error : {}'.format(e))

    def save_all_datas(self, datas):
        for data in datas:
            self.save_data(data)
        logging.info('---toutiao save ALL datas successfully---')

    def update_one_data(self, data):
        create_date = datetime.now()
        TouTiaoModel.objects(
            title=data['title']
        ).update_one(
            set__abstract=data['abstract'],
            set__chinese_tag=data['chinese_tag'],
            set__comments_count=data['comments_count'],
            set__label=data['label'],
            set__source_url=data['source_url'],
            set__release_time=data['release_time'].strftime('%Y-%m-%d %H:%M:%S'),
            set__crawl_time=create_date.strftime('%Y-%m-%d %H:%M:%S'),
            set__time_span=str(create_date - data['release_time']),
            upsert=True
        )
        logging.info('save one data, ok!')

    def update_all_datas(self, datas):
        for data in datas:
            self.update_one_data(data)
        logging.info('---toutiao save ALL datas successfully---')

    def get_data(self):
        model = TouTiaoModel
        data = model.objects.no_cache()
        return data

    def custom_fetching_data(self):
        model = TouTiaoModel
        datas = model.objects
        return datas


class ObserverOperation:
    def __init__(self):
        connect('db_web_data')
        logging.info('connect mongo: Observer successfully!')

    def save_data(self, data):
        create_date = datetime.now()
        observer = ObserverModel(
            title=data['title'],
            abstract=data['abstract'],
            chinese_tag=data['chinese_tag'],
            comments_count=data['comments_count'],
            label=data.get('label', []),
            source_url=data['source_url'],
            release_time=data['release_time'].strftime('%Y-%m-%d %H:%M:%S'),
            crawl_time=create_date.strftime('%Y-%m-%d %H:%M:%S'),
            time_span=str(create_date - data['release_time'])
        )
        try:
            observer.save()
            logging.info('observer save one data successfully.')
        except Exception as e:
            logging.info('observer failed to save one data | error : {}'.format(e))

    def save_all_datas(self, datas):
        for data in datas:
            self.save_data(data)
        logging.info('---observer save ALL datas successfully---')

    def update_one_data(self, data):
        create_date = datetime.now()
        ObserverModel.objects(
            title=data['title']
        ).update_one(
            set__abstract=data['abstract'],
            set__chinese_tag=data['chinese_tag'],
            set__comments_count=data['comments_count'],
            set__label=data['label'],
            set__source_url=data['source_url'],
            set__release_time=data['release_time'].strftime('%Y-%m-%d %H:%M:%S'),
            set__crawl_time=create_date.strftime('%Y-%m-%d %H:%M:%S'),
            set__time_span=str(create_date - data['release_time']),
            upsert=True
        )
        logging.info('save one data, ok!')

    def update_all_datas(self, datas):
        for data in datas:
            self.update_one_data(data)
        logging.info('---observer save ALL datas successfully---')

    def get_data(self):
        model = ObserverModel
        data = model.objects.no_cache()
        return data

    def custom_fetching_data(self):
        model = ObserverModel
        datas = model.objects
        return datas

class TencentOperation:
    def __init__(self):
        connect('db_web_data')
        logging.info('connect mongo: Tencent successfully!')

    def update_one_data(self, data):
        create_date = datetime.now()
        TencentModel.objects(
            title=data['title']
        ).update_one(
            set__abstract=data['abstract'],
            set__chinese_tag=data['chinese_tag'],
            set__comments_count=data['comments_count'],
            set__label=data['label'],
            set__source_url=data['source_url'],
            set__release_time=data['release_time'].strftime('%Y-%m-%d %H:%M:%S'),
            set__crawl_time=create_date.strftime('%Y-%m-%d %H:%M:%S'),
            set__time_span=str(create_date - data['release_time']),
            upsert=True
        )
        logging.info('save one data, ok!')

    def update_all_datas(self, datas):
        for data in datas:
            self.update_one_data(data)
        logging.info('---Tencent save ALL datas successfully---')

    def get_data(self):
        model = TencentModel
        data = model.objects.no_cache()
        return data

    def custom_fetching_data(self):
        model = TencentModel
        datas = model.objects
        return datas
