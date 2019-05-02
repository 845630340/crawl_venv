# -*- coding: utf-8 -*-

import jieba
import gensim
import re
from crawl_venv.crawl_data_to_mongo.mongo.operation import ObserverOperation
from gensim.models.doc2vec import Doc2Vec, TaggedDocument, TaggedLineDocument

def get_datas():
    ob = ObserverOperation()
    datas = ob.custom_fetching_data()
    return datas

# the count of datas is small
def get_model_small():
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
        model.save('title_model')


model = Doc2Vec.load('title_model')
print('finish loading the model')
# for i in range(1):
#     print(model.docvecs[str(i)])
print(model.docvecs.doctag_syn0)


