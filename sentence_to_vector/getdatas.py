from crawl_venv.crawl_data_to_mongo.mongo.operation import ObserverOperation

ob = ObserverOperation()
datas = ob.custom_fetching_data()
print(type(datas))
for i in datas[:10]:
    print(i.title)

# import jieba
#
# a = '我喜欢吃皮皮虾'
# res = jieba.cut(a)
# print(','.join(res))