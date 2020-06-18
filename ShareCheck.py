import sklearn
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation


stopwords = set(stopwords.words('portuguese') + list(punctuation))



def stopWordRemove(text):
    tokenized = word_tokenize(text)
    return [w for w in tokenized if w not in stopwords]


def shareRequest(files, dir):
    lines = []
    for fl in files:
        with open(dir+'/'+fl, 'r') as f:
            lines = stopWordRemove(f.read().lower())
            print(lines, "\n")


    pass

if __name__ == "__main__":
    shareRequest(None, None)