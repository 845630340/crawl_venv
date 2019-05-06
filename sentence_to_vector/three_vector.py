from .three_model import Model
from gensim.models.doc2vec import Doc2Vec

model = Model()

def get_title_vector():
    title_model = Doc2Vec.load('title_model')
    title_model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    with open('title_corpora.seq', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            pass