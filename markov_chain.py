import nltk
import numpy as np
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

# Get raw text as string.
corpusdir = 'lyrics/' # Directory of corpus.
oLedZeppelinCorpus = PlaintextCorpusReader(corpusdir, '.*')
lCorpus = oLedZeppelinCorpus.words() # every word in the corpus

def make_pairs(lCorpus):
    for i in range(len(lCorpus)-1):
        yield (lCorpus[i], lCorpus[i+1])
        
pairs = make_pairs(lCorpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
 
first_word = np.random.choice(lCorpus)

while first_word.islower():
    first_word = np.random.choice(lCorpus)

chain = [first_word]

n_words = 50

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print ' '.join(chain)