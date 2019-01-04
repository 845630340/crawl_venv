# -*- coding:utf8 -*-
from model import TouTiaoModel
import logging


class TouTiaoOperation:
    def save_data(self, data):
        toutiao = TouTiaoModel(
            title=data['title'],
            text=data['text'],
            date=data['date'],
            reading_count=data['reading_count']
        )
        toutiao.save()

    def save_all_datas(self, datas):
        for data in datas:
            try:
                self.save_data(data)
            except:
                logging.exception('happen error!')

    def get_data(self):
        model = TouTiaoModel
        data = model.objects.no_cache()
        return data
