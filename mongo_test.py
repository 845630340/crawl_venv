# -*- coding:utf8 -*-
from mongoengine import connect, Document
from mongoengine.fields import *


# connect the mongo locally
def connect_mongo(db_name):
    connect(db_name)


# the model of mongo collection
class JiangTestModel(Document):
    name = StringField(null=True, default='')
    age = IntField(null=True, default='20')
    meta = {
        'collection': 'collection_jiang'
    }


# save the data to collection model
def save_data(data):
    jiang = JiangTestModel(name=data['name'], age=data['age'])
    jiang.save()


if __name__ == '__main__':
    connect_mongo('db_jiang')
    datas = [{'name': 'xiaohong', 'age': 10}, {'name': 'xiaoming', 'age': 10}]
    for data in datas:
        save_data(data)

# synchronizer.py : 从Mongo中取数据rows,向Postgre中存数据cache
# ------ 取数据 ------
# 1.MongoSource.query() :                            根据collection_name连接MongoDB,返回查询数据（date）
# 2.MongoDB('apple_store_rating_data').query(date) : 从collection_name对应的mongo中取数据
# 3.得到rows

# ------ 存数据 ------
# 1.PostgreTarget.insert()：四个参数
#   db_name = ''
#   table_name = postgre-model模型
#   data = [{row},{row},{},{}]
#   tge_params = {'import_mode': 'UPDATEADD'}
# 2.
#
# ----------------------------------------------------
# ----------------------------------------------------
#
# ------ 同步的主线 ------
# self.syncer.connect : 连接mongo和postgre数据库
# self.syncer.run     : 取mongo数据，存入postgre
