import gensim
import numpy as np 
import pandas as pd 

cmuFrame = pd.read_csv("cmuFrame")

rhymingPairs = []
for row1 in cmuFrame.itertuples():
	for row2 in cmuFrame.itertuples():
		if (row1[0] != row2[0]):
			if (len(row1[2]) > 6) and (len(row2[2]) > 6):
				if (row1[2][-4:] == row2[2][-4:]):
					print(row1[0], row2[0])
