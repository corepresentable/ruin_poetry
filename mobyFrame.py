import pandas as pd 

path = "mobypos.txt"

mobyDict = []
with open(path, encoding="ISO 8859-1") as f:
	for line in f:
		word, pos = line.strip().split('\\')
		mobyDict.append((word, pos))


mobyFrame = pd.DataFrame(mobyDict)

mobyFrame.columns = ["word", "pos"]

print(mobyFrame.head())

print(mobyFrame["pos"][2])

mobyFrame.to_csv("mobyFrame", index = False)