# -*- coding:utf8 -*-
from mongoengine import connect, Document
from mongoengine.fields import *

def connect_mongo():
    connect('db_web_data')


class TouTiaoModel(Document):
    title = StringField(null=True, default='')
    text = StringField(null=True, default='')
    date = DateTimeField(null=True)
    reading_count = IntField(null=False)
    meta = {'collection': 'TouTiao'}