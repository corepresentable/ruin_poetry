import numpy as np 
import pandas as pd 


def rhymingPart(phones):
	idx = 0
	phones_list = phones.split()
	for i in reversed(range(0,len(phones_list))):
		if phones_list[i][-1] in ('1','2'):
			idx = i
			break
	rp =  ' '.join(i if not i[-1].isdigit() else i[0:len(i)-1] for i in phones_list[idx:])
	return rp

cmuFrame = pd.read_csv("cmuFrame2")

print(cmuFrame.head())

rhymes = []

for row in cmuFrame.itertuples():
#	print(row[2])
#	print(type(row[2]))
	rhyme = rhymingPart(row[2])
#	print(rhyme)
	rhymes.append(rhyme)

cmuFrame['rhyme'] = pd.Series(rhymes, index = cmuFrame.index)

print(cmuFrame.head(100))

cmuFrame.to_csv("rhymeFrame", index = False)
