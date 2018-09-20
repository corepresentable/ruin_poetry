import numpy as np
import pandas as pd

mobyFrame = pd.read_csv("mobyFrame")
rhymeFrame = pd.read_csv("rhymeFrame")

rhymeFrame['word'] = rhymeFrame['word'].astype(str)
mobyFrame['word'] = mobyFrame['word'].astype(str)
mobyFrame['word'] = mobyFrame['word'].apply(lambda x: x.upper())

mobyTest = mobyFrame[mobyFrame['word'] == "APOLOGETIC"]
rhymeTest = rhymeFrame[rhymeFrame['word'] == 'APOLOGETIC']

print(mobyTest)
print(rhymeTest)

wF = mobyFrame.join(rhymeFrame.set_index('word'), on='word')

wF = wF[pd.notnull(wF['pos'])]

wF = wF[pd.notnull(wF['pron'])]

wF = wF.reset_index(drop=True)
print(wF.head(1000))

wfTest = wF[wF['word'] == "ATMOSPHERIC"]

for adj in wF.head().itertuples():
	print(adj)
	for x in range(len(adj)):
		print(adj[x])

adjNoun = []

for adj in wF.itertuples():
	if adj[2] == "A":
		for noun in wF.itertuples():
			if noun[4] == adj[4]:
				if noun[1] != adj[1]:
					if noun[2] == "N":
						_rhymepair = adj[1] + " " + noun[1]
						adjNoun.append(adj[1] + " " + noun[1])
						print(_rhymepair)

outF = open("adjNoun.txt", 'w')
for rhyme in adjNoun:
	outF.write(rhyme)
	outF.write("\n")
outF.close()



					





