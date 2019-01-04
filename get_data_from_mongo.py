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


# get data from collection model
def get_data():
    model = JiangTestModel
    data = model.objects.no_cache()
    print 'the data is:', data
    for each in data:
        print each['name'], each['age']


# objects which is used to access the documents in the database collection associated with the class
# model.objects.no_cache()  // get the all data from the collection
# model.objects.count()     // get the collection data's count
# for each_docu in JiangTestModel.objects:
#     print each_docu['name']

if __name__ == '__main__':
    connect_mongo('db_jiang')
    get_data()
