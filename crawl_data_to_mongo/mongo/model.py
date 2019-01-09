# -*- coding:utf8 -*-
from mongoengine import connect, Document
from mongoengine.fields import *

def connect_mongo():
    connect('db_web_data')


class TouTiaoModel(Document):
    title = StringField(null=True, default='')
    abstract = StringField(null=True, default='')
    chinese_tag = StringField(null=True, default='')
    comments_count = IntField(null=False, default=0)
    label = ListField()
    source_url = StringField(null=True, default='')
    date = DateTimeField()

    meta = {'collection': 'TouTiao'}