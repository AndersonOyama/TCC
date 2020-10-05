import pandas as pd
import nltk


from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from pandas_ods_reader import read_ods
from pandas_ods_reader import read_ods
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

def sansaChecker(files, dir):

    list_share = []

    train_file = "./dataset/sensa/train_gen_sensa.ods"
    test_file = "./dataset/sensa/train_gen_sensa.ods"

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

            if (blob.classify() == 'sensacionalista'):
                prob_vec.append(round(prob_dist.prob('sensacionalista'), 2))
            else:
                prob_vec.append(round(prob_dist.prob('não sensacionalista'), 2))
            f.close()

    return list_share, accuracy, prob_vec


def removeStopWords(text, stopwords):


    return text

