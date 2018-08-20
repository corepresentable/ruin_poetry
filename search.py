import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('w2v', binary=True)

L = ["cat", "dog", "fish", "space force"]

print(model['dog'])

