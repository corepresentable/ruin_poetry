import gensim
import numpy as np 
import pandas as pd 


path = "cmudict-0.7b.txt"

cmuDict = []
with open(path, encoding="ISO 8859-1") as f:
	for line in f:
		word, pronunc = line.strip().split('  ')
		pronunc = pronunc.split(' ')
		cmuDict.append((word, pronunc))


cmuFrame = pd.DataFrame(cmuDict)

cmuFrame.columns = ["word", "pron"]

print(cmuFrame.head())

cmuFrame.to_csv("cmuFrame", index = False)