from nltk.tokenize import word_tokenize

import sklearn
stopwords = nltk.corpus.stopwords.words(‘portuguese’)


def shareRequest(file):
    with open(file, 'r') as f:
        lines = word_tokenize(f.read().lower())


if __name__ == "__main__":
    main()