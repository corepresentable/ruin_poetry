# ruin_poetry

adjNoun.txt is a list of rhyming pairs of words; the first an adjective, the second a noun. It is made from the CMU pronunciation dictionary (see adjNoun.py).

search.py imports the adjNoun.txt as a csv file, and also imports Google's word2vec model. It uses the word2vec model to transform the list of adjective+nouns into a list of vectors. The user is prompted to import a word, which is also transformed into a vector. It is then compared (for distance) against the list of adjective+noun vectors and presents the pairs of rhyming words which are closest to the input word.

adjective_Noun.py uses rhymeFrame and mobyFrame (both DataFrames) to determine whether two words rhyme (rhymeFrame) and whether a word is a noun or an adjective (mobyFrame).

rhymeFrame is built from CMU's pronunciation dictionary.
