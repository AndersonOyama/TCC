import pandas as pd
import nltk


from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from pandas_ods_reader import read_ods
from pandas_ods_reader import read_ods
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

def shareCheck(files, dir):

    list_share = []

    train_file = "./dataset/compartilhamento/train_gen_compartilhamento.ods"
    test_file = "./dataset/compartilhamento/train_gen_compartilhamento.ods"

    sheet_id = 1
    df = read_ods(train_file, sheet_id)
    df = pd.DataFrame(data=df)
    df.columns = ['Frase', 'Sentimento']

    train_file_records = df.to_records(index=False)


    clas = NaiveBayesClassifier(train_file_records)


    test_set_file = read_ods(test_file, sheet_id)
    test_set_file = pd.DataFrame(data=test_set_file)
    test_file_records = test_set_file.to_records(index=False)

    accuracy = clas.accuracy(test_file_records)
    prob_vec = []

    for f in files:
        with open(dir+f, 'r') as f:
            lines = f.read()
            
            blob = TextBlob(lines, classifier=clas)
            list_share.append(blob.classify())
            prob_dist = clas.prob_classify(lines)

            if (blob.classify() == 'compartilhamento'):
                prob_vec.append(round(prob_dist.prob('compartilhamento'), 2))
            else:
                prob_vec.append(round(prob_dist.prob('sem compartilhamento'), 2))
            # print("Texto: ", f, "Comp: ", round(prob_dist.prob("compartilhamento"),2), "Sem: ", round(prob_dist.prob("sem compartilhamento"),2))
            f.close()

    return list_share, accuracy, prob_vec


def removeStopWords(text, stopwords):


    return text

