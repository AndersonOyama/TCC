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

    train_file = "./dataset/compartilhamento/train_set.ods"
    test_file = "./dataset/compartilhamento/treino_compartilhamento.ods"

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

    frase = "O governo japonês decidiu se livrar de todos os fornos de microondas do país antes do final do ano. Todos os cidadãos e organizações que não cumpram este requisito enfrentam penas de prisão de 5 a 15 anos, dependendo da gravidade do crime. A razão para a proibição de microondas na terra do sol nascente é uma pesquisa realizada por cientistas da Universidade de Hiroshima, que descobriu que as ondas radioativas causaram mais danos à saúde dos cidadãos durante os 20 anos com o uso do forno de microondas que o bombardeamento nuclear de aviões americanos em setembro de 1945. De acordo com os resultados dos especialistas, os alimentos aquecidos em um forno de microondas apresentam vibrações adversas, em desacordo com os ritmos universais. Todos os principais fabricantes de fornos de microondas no Japão já fecharam suas instalações de fabricação. Em 2021, a fabricação de fornos de microondas será anunciada na Coréia do Sul. A China planeja abandonar esse tipo de tecnologia em 2023. Envie para as pessoas que você ama. Faça isso, porque bondade não custa nada"
    frase2 = "Publicados em revistas científicas internacionais, dois estudos liderados pela Fundação Oswaldo Cruz (Fiocruz) demonstram ação do antiviral sofosbuvir – medicamento usado no tratamento da hepatite C – em infecções por febre amarela e chikungunya. Os dados inéditos foram obtidos em testes com camundongos, considerados modelos para estudo dos agravos. Na infecção por febre amarela, o antiviral diminuiu a mortalidade e as lesões no fígado dos animais. Já nos casos de chikungunya, o sofosbuvir reduziu a mortalidade, a inflamação articular e as sequelas neurológicas. Os estudos foram liderados pelo grupo de cientistas que apontou, de foram pioneira, a ação do sofosbuvir sobre o vírus zika, em 2016. O artigo referente ao vírus da febre amarela foi divulgado no dia 30 de janeiro na revista científica Plos Neglected Infectious Diseases, enquanto o estudo sobre chikungunya foi publicado no dia 29 de janeiro na edição do periódico Antimicrobial Agentes and Chemotehrapy. Os dois estudos foram realizados em colaboração por quatro unidades da Fiocruz: Centro de Desenvolvimento Tecnológico em Saúde (CDTS), Instituto Oswaldo Cruz (IOC), Instituto Nacional de Infectologia Evandro Chagas (INI) e Instituto de Tecnologia em Fármacos (Farmanguinhos). A investigação sobre o vírus chikungunya teve ainda a cooperação com Instituto D’Or de Pesquisa (IDOR), Universidade Federal do Rio de Janeiro (UFRJ) e Consórcio BMK, formado pelas empresas Blanver Farmoquímica, Microbiológica Química e Farmacêutica e Karin Bruning. Já a pesquisa sobre o vírus da febre amarela foi feita em parceria com UFRJ e Universidade Federal de Minas Gerais (UFMG)."
    frase3 = "Não envie para seus amigos."
    # print(test_set_file.values.tolist())



    for f in files:
        with open(dir+f, 'r') as f:
            lines = f.read()
            blob = TextBlob(lines, classifier=clas)
            list_share.append(blob.classify())
    
    # print(list_share)
    return list_share


    # print('Esta frase é de caráter:{}'.format(blob.classify()))
    # print('Precisão da previsão:{}'.format(accuracy))



