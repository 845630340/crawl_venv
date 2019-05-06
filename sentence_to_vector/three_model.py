# -*- coding: utf-8 -*-

import jieba
import re
from crawl_venv.crawl_data_to_mongo.mongo.operation import ObserverOperation, TouTiaoOperation, TencentOperation
from gensim.models.doc2vec import Doc2Vec, TaggedLineDocument
from gensim.models.word2vec import Word2Vec


def get_toutiao_datas():
    ob = TouTiaoOperation()
    datas = ob.custom_fetching_data()
    return datas


def get_observer_datas():
    ob = ObserverOperation()
    datas = ob.custom_fetching_data()
    return datas


def get_tencent_datas():
    ob = TencentOperation()
    datas = ob.custom_fetching_data()
    return datas


class Model:

    def __init__(self):
        self.datas = [get_observer_datas(), get_tencent_datas(), get_toutiao_datas()]

    def get_title_model(self):

        # 结巴分词后的语料库---title
        with open('title_corpora.seq', 'a+', encoding='utf-8') as f:
            for data in self.datas:
                for index, item in enumerate(data):
                    title = item.title
                    title = re.sub("[！？，。“”——\s]", "", title)
                    words = jieba.cut(title)
                    f.write(' '.join(words) + '\n')
        print('--- finishing title_corpora ! ---')

        with open('title_corpora.seq', 'r', encoding='UTF-8') as f:
            sentences = TaggedLineDocument(f)  # the file should be opened
            model = Doc2Vec(sentences, dm=1, window=8, workers=4)  # the params have not been sure
            model.save('title_model')
        print('--- finishing title_model ! ---')

    def get_abstract_model(self):

        # 结巴分词后的语料库---abstract
        with open('abstract_corpora.seq', 'a+', encoding='utf-8') as f:
            for data in self.datas:
                for index, item in enumerate(data):
                    abstract = item.abstract
                    abstract = re.sub("[！？，。：“”——\s]", "", abstract)
                    words = jieba.cut(abstract)
                    f.write(' '.join(words) + '\n')
        print('--- finishing abstract_corpora ! ---')

        with open('abstract_corpora.seq', 'r', encoding='UTF-8') as f:
            sentences = TaggedLineDocument(f)  # the file should be opened
            model = Doc2Vec(sentences, dm=1, window=8, workers=4)  # the params have not been sure
            model.save('abstract_model')
        print('--- finishing abstract_model ! ---')

    def get_tag_model(self):
        tag_list = self.get_tag_list()

        model = Word2Vec(tag_list, size=100, window=5, min_count=1, workers=4)
        model.save('tag_model')
        print('--- finishing chinese_tag model ! ---')

    def get_tag_list(self):
        tag_list = []
        for each in self.datas:
            tag_list += each.distinct('chinese_tag')
        return tag_list




# model = Model()
# model.get_tag_model()

