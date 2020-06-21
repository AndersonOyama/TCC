import sklearn
import nltk

import pandas as pd

from pandas_ods_reader import read_ods
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation


train_file = "./dataset/compartilhamento/treino_compartilhamento.ods"

stopwords = set(stopwords.words('portuguese') + list(punctuation))
stemmer = nltk.stem.RSLPStemmer



def stopWordRemove(text):
    tokenized = word_tokenize(text)
    text_tokenized = [w for w in tokenized if w not in stopwords]
    text_stemmer = [stemmer.stem(word) for word in text_tokenized]
    pass    



def shareRequest(files, dir):
    sheet_id = 1
    lines = []
    # classification = read_ods()
    df = read_ods(train_file, sheet_id)
    df = pd.DataFrame(data=df)
    df.columns = ['Frase', 'Ação']


    classificador = nltk.classify.NaiveBayesClassifier.train(df)
    print(classificador.labels())
    
    

    for fl in files:
        with open(dir+'/'+fl, 'r') as f:
            lines = stopWordRemove(f.read().lower())
            


    pass

if __name__ == "__main__":
    shareRequest(None, None)