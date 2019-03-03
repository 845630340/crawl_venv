# -*- coding:utf8 -*-
from mongoengine import connect, Document
from mongoengine.fields import *


def connect_mongo():
    connect('db_web_data')


class TouTiaoModel(Document):
    title = StringField(null=True, default='')  # null = True : the value of field cannot be empty,must set a value.
    abstract = StringField(null=True, default='')
    chinese_tag = StringField(null=True, default='')
    comments_count = IntField(null=True, default=0)
    label = ListField()
    source_url = StringField(null=True, default='')
    release_time = DateTimeField(required=True)
    crawl_time = DateTimeField(required=True)
    time_span = StringField(required=True)

    meta = {
        'collection': 'TouTiao',
        'indexes': [
            {
                'fields': ['title'],
                'unique': True
            }
        ]
    }


class ObserverModel(Document):
    title = StringField(null=True, default='')
    abstract = StringField(null=True, default='')
    chinese_tag = StringField(null=True, default='')
    comments_count = IntField(null=True, default=0)
    label = ListField()
    source_url = StringField(null=True, default='')
    release_time = DateTimeField(required=True)
    crawl_time = DateTimeField(required=True)
    time_span = StringField(required=True)

    meta = {
        'collection': 'Observer',
        'indexes': [
            {
                'fields': ['title'],
                'unique': True
            }
        ]
    }


class TencentModel(Document):
    title = StringField(null=True, default='')
    abstract = StringField(null=True, default='')
    chinese_tag = StringField(null=True, default='')
    comments_count = IntField(null=True, default=0)
    label = ListField()
    source_url = StringField(null=True, default='')
    release_time = DateTimeField(required=True)
    crawl_time = DateTimeField(required=True)
    time_span = StringField(required=True)

    meta = {
        'collection': 'Tencent',
        'indexes': [
            {
                'fields': ['title'],
                'unique': True
            }
        ]
    }