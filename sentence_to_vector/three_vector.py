# -*- coding: utf-8 -*-

import csv
from crawl_venv.sentence_to_vector.three_model import Model
from gensim.models.doc2vec import Doc2Vec
from gensim.models.word2vec import Word2Vec

model = Model()


def get_title_vector():
    title_model = Doc2Vec.load('title_model')
    title_model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    title_vectors = []
    with open('title_corpora.seq', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            vector = title_model.infer_vector(line.split())
            title_vectors.append(vector.mean())
    return title_vectors


def get_abstract_vector():
    abstract_model = Doc2Vec.load('abstract_model')
    abstract_model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    abstract_vectors = []
    with open('abstract_corpora.seq', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            vector = abstract_model.infer_vector(line.split())
            abstract_vectors.append(vector.mean())
    return abstract_vectors


def get_tag_vector():
    tag_model = Word2Vec.load('tag_model')
    tag_model.delete_temporary_training_data(replace_word_vectors_with_normalized=True)

    tag_vectors = []
    tag_list = model.get_tag_list(distinct=False)
    for each in tag_list:
        vector = tag_model.wv[each].mean()
        tag_vectors.append(vector)
    return tag_vectors


def get_hot_list():
    values = []
    for each in model.datas:
        for item in each:
            span = item.crawl_time - item.release_time
            counts = item.comments_count
            hours = round(span.total_seconds() / 3600)
            if hours == 0:
                value = counts
            else:
                value = round(counts / hours)
            values.append(value)
    hot = []
    for v in values:
        if v >= 3000:
            hot.append(1)
        else:
            hot.append(0)
    return hot


def create_csv():
    title_vectors = get_title_vector()
    abs_vectors = get_abstract_vector()
    tag_vectors = get_tag_vector()
    hot_list = get_hot_list()
    rows = zip(title_vectors, abs_vectors, tag_vectors, hot_list)
    with open('datasets.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    print('--- finishing datasets.csv ! ---')

create_csv()

'''
1.解决了空行问题，但还没生成新的数据集，目前的数据集有空行
2.要在首行加名称？看看__init__.py文件代码
'''