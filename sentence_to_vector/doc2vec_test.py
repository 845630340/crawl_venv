# -*- coding: utf-8 -*-

import jieba
import re
from crawl_venv.crawl_data_to_mongo.mongo.operation import ObserverOperation
from gensim.models.doc2vec import Doc2Vec, TaggedDocument, TaggedLineDocument

def get_datas():
    ob = ObserverOperation()
    datas = ob.custom_fetching_data()
    return datas

# the count of datas is small
def get_model_small():
    datas = get_datas()
    documents = []
    count = 0
    for i in datas[:10]:
        title = i.title
        title = re.sub("[！？，。“”——\s]", "", title)  # remove punctuations and spaces
        print(title)
        words = jieba.lcut(title)
        print(words)
        documents.append(TaggedDocument(words, [str(count)]))
        count += 1

    model = Doc2Vec(documents, dm=1, window=8,  workers=4)
    model.save('title_model_small')


# the count of datas is large
def get_model_big():
    datas = get_datas()
    with open('corpora1.seq', 'a+') as f:
        for index, item in enumerate(datas[:10]):
            title = item.title
            title = re.sub("[！？，。“”——\s]", "", title)
            words = jieba.cut(title)
            f.write(' '.join(words)+'\n')

    with open('corpora1.seq', 'r') as f:
        sentences = TaggedLineDocument(f)  # the file should be opened
        model = Doc2Vec(sentences, dm=1, window=8,  workers=4)  # the params have not been sure
        model.save('title_model_test')

    print('product the model successfully!')


# get_model_big() # 生成model

# model = Doc2Vec.load('title_model_test')
# model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
# print('finish loading the model')
#
# print(model.docvecs.vectors_docs[0])
# text = '顶 着 美国 压力 法国参议院 把 这事否 了'.split()
# vector = model.infer_vector(text)
# print(vector.mean()) # 获得一个句向量


# 取数据集数据，用作逻辑回归模型输入
# from crawl_venv.sentence_to_vector import load_iris
# dataset = load_iris()
# print(dataset.data[:3, :2])


import csv
with open('iris.csv', 'r') as f:
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    print(final_list[:3, :2])
