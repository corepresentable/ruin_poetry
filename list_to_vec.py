import numpy as np
import pandas as pd
import pickle
import gensim

path = "adjNoun.txt"

model = gensim.models.KeyedVectors.load_word2vec_format('~/W2V/w2v', binary=True)

adjNoun = pd.read_csv(path, sep="\n", header=None)
adjNoun = adjNoun[0].tolist()

vecAN = []
for rhyme in adjNoun:
	rhyme = rhyme.lower()
	words = rhyme.split(" ")
	if (words[0] in model) and (words[1] in model):
		print(rhyme)
		vec = model[words[0]] + model[words[1]]
		print(vec[0:20])
		vecAN.append([rhyme, vec])

with open('vecAN.pkl', 'wb') as f:
	pickle.dump(vecAN, f)


