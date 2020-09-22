import sklearn
import nltk

import pandas as pd

from pandas_ods_reader import read_ods
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation



train_file = "./dataset/compartilhamento/treino_compartilhamento.ods"

stopwords = set(stopwords.words('portuguese') + list(punctuation))
stemmer = nltk.stem.RSLPStemmer()

unique_words_train = []

def stopWordRemoveAndStem(text):
    phrase = []
    for i in range(0, len(text), 1):
        noStop = [p for p in text.values[i,0].split() if p not in stopwords]
        noStem = [stemmer.stem(word) for word in noStop]
        # print("\t", noStem, "\n")
        phrase.append((noStem, text.values[i, 1]))
    return phrase

def list_all_words(text):
    words_list = []
    for (index, words,  feeling) in text.itertuples():
        words_list.extend(words)
    return words_list

def most_frequency(text):
    return nltk.FreqDist(text)

def uniqueWords_text(text):
    return text.keys() 

def extract_words(text):
    doc = set(text)
    character = {}
    for words in unique_words_train:
        character['$s' % words] = (words in doc)
    return character



def shareRequestTrain(files, dir):
    sheet_id = 1
    lines = []
    df = read_ods(train_file, sheet_id)
    df = pd.DataFrame(data=df)
    df.columns = ['Frase', 'Sentimento']
    lines = stopWordRemoveAndStem(df)

    train_text = pd.DataFrame(lines, columns=['Frase', 'Sentimento'])
    # print("\n\n", train_text)
    
    words_train = list_all_words(train_text)
    freq_train = most_frequency(words_train)
    # print("frequente: ", freq_train.most_common(10))   
    
    unique_words_train = uniqueWords_text(freq_train)
    # print(unique_words_train)

    base_treino = nltk.classify.apply_features(extract_words([]) ,words_train)
    print(base_treino)
    print(unique_words_train)
    classificador = nltk.NaiveBayesClassifier.train(base_treino)
    print(classificador.labels())
    # train = nltk.NaiveBayesClassifier.train(train_text)

    # classificador = nltk.classify.NaiveBayesClassifier.train(lines)
    # print(classificador.labels())
    
    

    # for fl in files:
    #     with open(dir+'/'+fl, 'r') as f:
    #         lines = stopWordRemove(f.read().lower())
            


    pass

if __name__ == "__main__":
    shareRequest(None, None)