import gensim
import numpy as np 
import operator as op 




#load the model (takes forever!!)

model = gensim.models.KeyedVectors.load_word2vec_format('~/W2V/w2v', binary=True)

#list of words
L = ['cat', 'dog', 'space', 'ennervate', 'call']


#initiate large numpy vector
big = 10000

#initiate a word vector
v = model["telephone"]


#add distances to wordlist
def dModel(L, vector):
	dlist = [],
	for w in L:
		try:
			_vec = model[w]
			_dist = np.linalg.norm(_vec - vector)
			dlist.append((w, _dist))
		except KeyError:
			dlist.append((w, big))
	return dlist

def topN(dL,N):
	topN = sorted(dL, key=op.itemgetter(1), reverse=False)[:N]
	return topN









