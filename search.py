import pickle
import numpy as np 
import pandas as pd
import operator as op 
import gensim

path = "adjNoun.txt"
adjNoun = pd.read_csv(path, sep="\n", header=None)
L = adjNoun[0].tolist()
print(len(L))


model = gensim.models.KeyedVectors.load_word2vec_format('~/W2V/w2v', binary=True)


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
    phrase = input().strip().split()
    vec = np.zeros(300)
    vecList = []
    svecList = []
    for word in phrase:
        try:
            vec = vec + model[word]
        except KeyError:
            print("'", word, "' is not currently in our vocabulary.")
    vec = vec * (1/len(phrase))      
    vecList = dModel(vec)
    svecList = topN(vecList, 100)
    for rhyme in svecList:
        print(rhyme)








