import os
import nltk
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from nltk.corpus.reader.plaintext import PlaintextCorpusReader

stop_words = set(stopwords.words('english')) # not interested in stop words
stop_words.update(['.', ',', "',", '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '-']) # ... or punctuation

corpusdir = 'lyrics/' # Directory of corpus.
oLedZeppelinCorpus = PlaintextCorpusReader(corpusdir, '.*')

lNoStopWords = []
for sWord in oLedZeppelinCorpus.words():
    if sWord not in stop_words:
        lNoStopWords.append(sWord)

lNoStopWordsLength = len(lNoStopWords)
wordCounts = Counter(lNoStopWords)
wordCountsLower = Counter(i.lower() for i in lNoStopWords)

# top 25
lCountLabels, lCountValues = zip(*wordCountsLower.most_common(50)[0:25])
lCountIndexes = np.arange(len(lCountLabels))
iCountWidth = 1
barlist = plt.bar(lCountIndexes, lCountValues)
for i in range(0, len(barlist)): # all bars to black
    barlist[i].set_color('black')
plt.xticks(lCountIndexes, lCountLabels)
plt.title("Word Occurrences in Led Zeppelin Lyrics")
plt.ylabel('Number of Occurrences Across All Songs')
plt.xlabel('Lyric')
plt.show()

# next 25
lCountLabels, lCountValues = zip(*wordCountsLower.most_common(50)[25:50])
lCountIndexes = np.arange(len(lCountLabels))
iCountWidth = 1
barlist = plt.bar(lCountIndexes, lCountValues)
for i in range(0, len(barlist)): # all bars to black
    barlist[i].set_color('black')
plt.xticks(lCountIndexes, lCountLabels)
plt.title("Word Occurrences in Led Zeppelin Lyrics")
plt.ylabel('Number of Occurrences Across All Songs')
plt.xlabel('Lyric')
plt.show()

# lPercentageLabels, lPercentageValues = zip(*wordCountsLower.most_common(25))
# lPercentageValues = [(iPercentageValue / lNoStopWordsLength * 100) for iPercentageValue in lPercentageValues] # calculate percentage
# 
# lPercentageIndexes = np.arange(len(lPercentageLabels))
# iPercentageWidth = 1
# plt.bar(lPercentageIndexes, lPercentageValues, iPercentageWidth)
# plt.xticks(lPercentageIndexes + iPercentageWidth * 0.5, lPercentageLabels)
# plt.show()