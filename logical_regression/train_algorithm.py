# -*- coding: utf-8 -*-

import jieba
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from crawl_venv.sentence_to_vector import load_iris
from sklearn.preprocessing import StandardScaler
from gensim.models.doc2vec import Doc2Vec
from gensim.models.word2vec import Word2Vec


# 1. 加载数据
datasets = load_iris()
x = datasets.data[:, :3]
y = datasets.target
print('加载数据完成。')


# 2. 拆分训练集、测试集
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print('拆分数据集完成。')

# 3.标准化特征值
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
print('标准化特征值完成。')

# 4. 训练逻辑回归模型
log_reg = linear_model.LogisticRegression()
log_reg.fit(X_train, Y_train)
print('训练逻辑回归模型完成。')

# 5. 预测
prepro = log_reg.predict_proba(X_test_std)
acc = log_reg.score(X_test_std, Y_test)

print(acc)
res = log_reg.predict(x[:, :3])


def func(title, tag):
    # 实战
    t = jieba.lcut(title)
    title_model = Doc2Vec.load('../sentence_to_vector/title_model')
    title_vector = title_model.infer_vector(t).mean()

    abs = title
    a = jieba.lcut(abs)
    abs_model = Doc2Vec.load('../sentence_to_vector/abstract_model')
    abs_vector = abs_model.infer_vector(a).mean()

    tag_model = Word2Vec.load('../sentence_to_vector/tag_model')
    tag_vector = tag_model.wv[tag].mean()

    x_new = np.array([title_vector, abs_vector, tag_vector]).reshape(1, -1)
    print(log_reg.predict(x_new))

# func('我正在写代码', 'internation')




