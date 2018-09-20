import gensim
import numpy as np 
import pandas as pd 


path = "cmudict-0.7b.txt"

cmuDict = []
with open(path, encoding="ISO 8859-1") as f:
	for line in f:
		word, pronunc = line.strip().split('  ')
		pron = "".join(pronunc)
		cmuDict.append((word, pron))


cmuFrame = pd.DataFrame(cmuDict)

cmuFrame.columns = ["word", "pron"]

print(cmuFrame.head())

print(cmuFrame["pron"][2])

cmuFrame.to_csv("cmuFrame2", index = False)