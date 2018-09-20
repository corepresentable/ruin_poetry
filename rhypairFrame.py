#!/Users/jbot/miniconda3/bin/python

import gensim
import numpy as np 
import pandas as pd 

cmuFrame = pd.read_csv("cmuFrame")



rhymingPairs = []
for row1 in cmuFrame.head(1000).itertuples():
	for row2 in cmuFrame.head(1000).itertuples():
		# if not the same word
		if (row1[0] != row2[0]):
			#if long enough
			#getting string instead of list
			#has something to do with how panda is getting data
			if (len(row1[1]) > 4) and (len(row2[1]) > 4 ):
				#if rhyming
				if (row1[2][-7:] == row2[2][-7:]):
					if (row1[2] != row2[2]):
						rhyme = [row1[1], row2[1]]
						#rhymingPairs.append(rhyme)
						#print(rhyme)
						print(rhyme)






					
