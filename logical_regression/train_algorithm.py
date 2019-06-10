# -*- coding: utf-8 -*-

import jieba
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from crawl_venv.sentence_to_vector import load_iris
from sklearn.preprocessing import StandardScaler
from gensim.models.doc2vec import Doc2Vec
from gensim.models.word2vec import Word2Vec
from sklearn.externals import joblib


def get_clf():
    # 1. 加载数据
    datasets = load_iris()
    x = datasets.data[:, :3]
    y = datasets.target
    print('加载数据完成。')

    # 2. 拆分训练集、测试集
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    print('拆分数据集完成。')

    # 3.标准化特征值
    # sc = StandardScaler()
    # sc.fit(X_train)
    # X_train_std = sc.transform(X_train)
    # X_test_std = sc.transform(X_test)
    # print('标准化特征值完成。')

    # 4. 训练逻辑回归模型
    log_reg = linear_model.LogisticRegression()
    log_reg.fit(X_train, Y_train)
    print('训练逻辑回归模型完成。')
    joblib.dump(log_reg, "train_model.m")
    print('模型已保存到本地')

# get_clf()

def get_acc():
    datasets = load_iris()
    x = datasets.data[:, :3]
    y = datasets.target
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    sc = StandardScaler()
    sc.fit(X_train)
    X_test_std = sc.transform(X_test)
    log_reg = joblib.load("train_model.m")
    acc = log_reg.score(X_test_std, Y_test)
    print('-------------------------------------------')
    print('该逻辑回归模型的精确度为：', acc)
    print('-------------------------------------------')


def func(title, abs, tag):
    # 实战
    t = jieba.lcut(title)
    title_model = Doc2Vec.load('../sentence_to_vector/title_model')
    title_vector = title_model.infer_vector(t).mean()

    a = jieba.lcut(abs)
    abs_model = Doc2Vec.load('../sentence_to_vector/abstract_model')
    abs_vector = abs_model.infer_vector(a).mean()

    tag_model = Word2Vec.load('../sentence_to_vector/tag_model')
    tag_vector = tag_model.wv[tag].mean()

    x_new = np.array([title_vector, abs_vector, tag_vector]).reshape(1, -1)
    log_reg = joblib.load("train_model.m")
    res = log_reg.predict(x_new)
    if res[0] == 0:
        print('This news is hot.')

title = '马克思墓碑被砸坏，英国网民怒了'
abs = '马克思出生于德国小镇特里尔，死后葬在\
英国伦敦海格特公墓。而在近日，马克思的墓被人砸了'
tag = 'internation'
func(title, abs, tag)




