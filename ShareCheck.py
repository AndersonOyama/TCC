import sklearn
import nltk

from nltk.corpus import stopwords
from string import punctuation


stopwords = set(stopwords.words('portuguese') + list(punctuation))


def shareRequest(file):
    with open(file, 'r') as f:
        lines = word_tokenize(f.read().lower())


if __name__ == "__main__":
    shareRequest(None)