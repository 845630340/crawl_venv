# -*- coding:utf8 -*-

import pymongo

# myclient = pymongo.MongoClient('localhost', 27017)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['db_jiang']
mycol = mydb['collection_jiang']

data = {'name': 'jiang', 'age': 12}
x = mycol.insert_one(data)
print x
