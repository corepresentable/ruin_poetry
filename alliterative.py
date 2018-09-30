import numpy as np
import pandas as pd

def first_sound(s):
	i = s.find(" ")
	return s[0:i]


def create_allit(s):
	allit = []
	for adj in wF.itertuples():
		if adj[2] == "A":
			for noun in wF.itertuples():
				if noun[3] == adj[3] == s:
					if noun[1] != adj[1]:
						if noun[2] == "N":
							_allit_pair = adj[1] + " " + noun[1]
							allit.append(_allit_pair)
							print(_allit_pair)
	return allit

mobyFrame = pd.read_csv("mobyFrame")
rhymeFrame = pd.read_csv("rhymeFrame")

print("Moby size is:", mobyFrame.shape)
print("rhyme size is:", rhymeFrame.shape)


#fix type
rhymeFrame['word'] = rhymeFrame['word'].astype(str)
#remove numbers from pronunciation
rhymeFrame['pron'] = rhymeFrame['pron'].apply(lambda x: ''.join([i for i in x if not i.isdigit()]))
#first sound
rhymeFrame['pron'] = rhymeFrame['pron'].apply(lambda x: first_sound(x))
#fix type
mobyFrame['word'] = mobyFrame['word'].astype(str)
#change to uppercase
mobyFrame['word'] = mobyFrame['word'].apply(lambda x: x.upper())



wF = mobyFrame.join(rhymeFrame.set_index('word'), on='word')

wF = wF[pd.notnull(wF['pos'])]

wF = wF[pd.notnull(wF['pron'])]

wF = wF.reset_index(drop=True)

wF.columns = ['first' if x == 'pron' else x for x in wF.columns]

print(wF.head())

print("wordFrame size is:", wF.shape)

phonemes = ["AA", "AE","AH", "AO", "AW", "AY", "B", "CH", "D","DH","EH","ER","EY","F","G",
"HH","IH","IY","JH","K","L","M","N","NG", "OW","OY","P","R","S","SH","T","TH","UH",
"UW","V","W","Y","Z","ZH"]

for phoneme in phonemes:
	allit_list = create_allit(phoneme)

exit_path = "allit" + "_" + phoneme + ".txt"

outF = open(exit_path, 'w')
for pair in allit_list:
	outF.write(pair)
	outF.write("\n")
outF.close()



					





