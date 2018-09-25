import pickle
import numpy as np 
import pandas as pd
import operator as op 
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('~/W2V/w2v', binary=True)
path = "adjNoun.txt"
adjNoun = pd.read_csv(path, sep="\n", header=None)
L = adjNoun[0].tolist()


#initiate large numpy vector
big = 100


#add distances to wordlist
def dModel(vector):
	dlist = []
	for rhyme in L:
		try:
			w = rhyme
			rhyme = rhyme.lower()
			word = rhyme.split(" ")
			_vec = ( model[word[0]] + model[word[1]] ) * 0.5
			_dist = np.linalg.norm(_vec - vector)
			dlist.append([w, _dist])
		except KeyError:
			dlist.append([w, big])
	return dlist

def topN(dL,N):
	topN = sorted(dL, key=op.itemgetter(1), reverse=False)[:N]
	return topN

while True:
	print("Enter a word:")
	word = input()
#initiate a word vector
	vec = model[word]
	vecList = dModel(vec)
	svecList = topN(vecList, 20)
	print(svecList)








