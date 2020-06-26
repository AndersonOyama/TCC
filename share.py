import pandas as pd
import nltk


from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from pandas_ods_reader import read_ods
from pandas_ods_reader import read_ods
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

def stopWordRemoveAndStem(text):
    phrase = []
    for i in range(0, len(text), 1):
        noStop = [p for p in text.values[i,0].split() if p not in stopwords]
        noStem = [stemmer.stem(word) for word in noStop]
        # print("\t", noStem, "\n")
        phrase.append((noStem, text.values[i, 1]))
    return phrase


stopwords = set(stopwords.words('portuguese') + list(punctuation))
stemmer = nltk.stem.RSLPStemmer()

train_file = "./dataset/compartilhamento/train_set.ods"
test_file = "./dataset/compartilhamento/treino_compartilhamento.ods"

sheet_id = 1
df = read_ods(train_file, sheet_id)
df = pd.DataFrame(data=df)
df.columns = ['Frase', 'Sentimento']

train_file_records = df.to_records(index=False)
# print(temp)

train = [
    ("Compartilhe esta informação!", "compartilhamento"),
    ("Não deixe de compartilhar esta informação!", "compartilhamento"),
    ("Não guarde essa informação para si. Compartilhe com seus amigos e familiares", "compartilhamento"),
    ("A gente sofre menos porque tem condições de tratar”, comentou a aposentada Maria Aparecida Vieira.", "sem compartilhamento"),
    ("Transmita essa informação para outras pessoas.", "compartilhamento"),
    ("Mande para frente essa informação.", "compartilhamento"),
    ("O local provável de infecção de um dos óbitos permanece em investigação.", "sem compartilhamento"),
    ("Por favor, passe isso adiante.", "compartilhamento"),
    ("Desta forma, além dos cuidados relativos à vacinação, todos os protocolos e notas técnicas relativas à COVID-19 serão observados.", "sem compartilhamento"),
    ("A terapia está disponível em 109 serviços de 90 municípios em 22 estados e no Distrito Federal. Desde a implantação da prevenção, cerca de oito mil pessoas já fizeram uso da prevenção ao menos uma vez. Atualmente, mais de seis mil pessoas fazem uso da PreP.", "sem compartilhamento"),
    ("Espalhe essa mensagem para a maior quantidade possível de pessoas.", "compartilhamento"),
    ("Repassem", "compartilhamento"),
    ("Compartilhe", "compartilhamento"),
    ("Quanto mais tempo demorar para resolver o problema que a causa, maior vai ser a crise econômica.", "sem compartilhamento"),
    ("Transmitam", "compartilhamento"),
    ("envie", "compartilhamento"),
    ("Não escondam essa mensagem, compartilhem", "compartilhamento"),
    ("A gente sofre menos porque tem condições de tratar”, comentou a aposentada Maria Aparecida Vieira.", "sem compartilhamento")
]

clas = NaiveBayesClassifier(train_file_records)

test_set = [
("Por favor não guarde isto para você. Repasse para ajudar outras pessoas.", "compartilhamento"),
("E se puder mande pra frente.", "compartilhamento"),
("Espalhe e você salvará a vida.", "compartilhamento"),
("Por favor, não esconda a mensagem ", "compartilhamento"),
("Não guarde essas informações apenas para si mesmo.", "compartilhamento"),
("Passe para toda a sua família e amigos.", "compartilhamento"),
("Repassem!", "compartilhamento"),
("Repasse para seus amigos e parentes para que eles saibam a que estão expostos com o uso desses venenos modernos.", "compartilhamento"),
("Se for possivel partilhem alertem as pessoas que amam", "compartilhamento"),
("Por favor, compartilhe essa informação.", "compartilhamento"),
("e vamos repassando essa dica ótima.", "compartilhamento"),
("Por favor, repassem essa informação.", "compartilhamento"),
("se todos que receberem esta mensagem, a enviarem a pelo menos uma das pessoas que conhecem", "compartilhamento"),
("Compartilhe esta mensagem com seus amigos e familiares para conscientizá-los sobre", "compartilhamento"),
("COMPARTILHE-O", "compartilhamento"),
("Repasse para seus famíliares e amigos pois é muito importante.", "compartilhamento"),
("Por favor, passe isso imediatamente.", "compartilhamento"),
("Por favor, não deixem de repassar esta mensagem para todos que vocês conhecem!", "compartilhamento"),
("compartilhe com os outros para espalhar o amor!", "compartilhamento"),
("Compartilhe esta mensagem com qualquer mulher que você conheça.", "compartilhamento"),
("Tem a missão de mobilizar a sociedade para que os pacientes tenham acesso a um tratamento integral e de qualidade, sendo reabilitados, incluídos na sociedade e tendo plena noção dos seus direitos básicos.", "sem compartilhamento"),
("Mas agências reguladoras de remédios dos Estados Unidos, do Reino Unido e da União Europeia, além da Reckitt Benckiser, a fabricante do Nurofen, disseram não haver indícios de que o ibuprofeno agrava a covid-19. ", "sem compartilhamento"),
("A gente sofre menos porque tem condições de tratar”, comentou a aposentada Maria Aparecida Vieira.", "sem compartilhamento"),
("No entanto, diz ela à BBC, \"existe um limite para o que os genomas podem ajudar a explicar\".", "sem compartilhamento"),
("Não é necessário incinerar ou descartar os pertences do falecido, mas devem ser tomadas precauções como manuseio com luvas e lavagem com detergente, além de desinfetar objetos com álcool ou alvejante.", "sem compartilhamento"),
("Enquanto isso, os especialistas aconselham que a melhor dieta vegana é aquela que inclui muitas frutas e vegetais, suplementos de vitamina B12 e menos frituras e alimentos processados.", "sem compartilhamento"),
("Aproximadamente metade dos residentes dessas instituições sofre com demência, com base em estimativas da Alzheimer's Association.", "sem compartilhamento"),
("O desafio, agora, será indentificar também quais dessas mutações se transformarão num câncer e quais poderiam ser ignoradas com segurança.", "sem compartilhamento"),
("O local provável de infecção de um dos óbitos permanece em investigação.", "sem compartilhamento"),
("Os exercícios físicos devem fazer parte do tratamento, de acordo com as possibilidades do paciente. Eles contribuem para a melhora da função respiratória, ajudam no ganho de massa muscular, controlam a diabetes relacionada à fibrose cística e previnem a osteoporose, além de atuar na correção de alguns vícios de postura adquiridos por conta dos problemas respiratórios.", "sem compartilhamento"),
("A pesquisa procurou ainda levar em conta outros fatores além dos hábitos cotidianos, como o histórico médico familiar dos participantes, etnia e idade, que também podem ter tido impacto nos resultados.", "sem compartilhamento"),
("A hemofilia ainda não tem cura e seu tratamento é feito através da reposição do fator de coagulação deficiente, através da infusão endovenosa dos concentrados de fator deficiente (VIII, na hemofilia A ou IX, na hemofilia B), que tem como objetivo prevenir e tratar as hemorragias.", "sem compartilhamento"),
("Agora, os autores do artigo na Nature Medicine querem verificar com a mesma técnica se também há anormalidades detectadas nas células de pacientes com outros perfis, como aqueles com mais de 50 anos de idade.", "sem compartilhamento"),
("Em 2018, foram investidos mais de R$ 279 milhões para aquisição de medicamentos para tratamento da doença no SUS, atendendo 15.689 usuários. Os medicamentos já ofertados são: betainterferona 1a 6.000.000 UI (22 mcg); betainterferona 1a 6.000.000 UI (30 mcg); betainterferona 1a 12.000.000 UI (44 mcg); betainterferona 1b 9.600.000 UI (300 mcg); fingolimode 0,5mg, glatirâmer 20mg/mL e natalizumabe 20mg/ml.", "sem compartilhamento"),
("A decisão ocorreu porque estudos científicos recentes demonstraram uma diminuição na resposta imunológica da criança que é vacinada muito cedo, aos 9 meses, como previa o Calendário Nacional de Vacinação da criança. Desde 2017, o Ministério da Saúde seguia as orientações da Organização Mundial da Saúde (OMS) de ofertar apenas uma dose da vacina de febre amarela durante toda a vida.", "sem compartilhamento"),
("Desta forma, além dos cuidados relativos à vacinação, todos os protocolos e notas técnicas relativas à COVID-19 serão observados.", "sem compartilhamento"),
("É importante frisar que todos os estados brasileiros recebem doses para vacinação de rotina contra sarampo, que é ofertada nos postos de saúde de todo o país pelo Sistema Único de Saúde (SUS).", "sem compartilhamento"),
("A terapia está disponível em 109 serviços de 90 municípios em 22 estados e no Distrito Federal. Desde a implantação da prevenção, cerca de oito mil pessoas já fizeram uso da prevenção ao menos uma vez. Atualmente, mais de seis mil pessoas fazem uso da PreP.", "sem compartilhamento"),
("Do total de casos que já tiveram a subtipagem identificada, 334 foram casos de influenza A (H1N1), com 41 óbitos; 29 casos e 4 óbitos por influenza A (H3N2), 180 de influenza A não subtipado, com 25 mortes; e 310 casos e 30 óbitos por influenza B.", "sem compartilhamento"),
("Quanto mais tempo demorar para resolver o problema que a causa, maior vai ser a crise econômica.", "sem compartilhamento")
]

test_set_file = read_ods(test_file, sheet_id)
test_set_file = pd.DataFrame(data=test_set_file)
test_file_records = test_set_file.to_records(index=False)

accuracy = clas.accuracy(test_file_records)

frase = "O governo japonês decidiu se livrar de todos os fornos de microondas do país antes do final do ano. Todos os cidadãos e organizações que não cumpram este requisito enfrentam penas de prisão de 5 a 15 anos, dependendo da gravidade do crime. A razão para a proibição de microondas na terra do sol nascente é uma pesquisa realizada por cientistas da Universidade de Hiroshima, que descobriu que as ondas radioativas causaram mais danos à saúde dos cidadãos durante os 20 anos com o uso do forno de microondas que o bombardeamento nuclear de aviões americanos em setembro de 1945. De acordo com os resultados dos especialistas, os alimentos aquecidos em um forno de microondas apresentam vibrações adversas, em desacordo com os ritmos universais. Todos os principais fabricantes de fornos de microondas no Japão já fecharam suas instalações de fabricação. Em 2021, a fabricação de fornos de microondas será anunciada na Coréia do Sul. A China planeja abandonar esse tipo de tecnologia em 2023. Envie para as pessoas que você ama. Faça isso, porque bondade não custa nada"
frase2 = "Publicados em revistas científicas internacionais, dois estudos liderados pela Fundação Oswaldo Cruz (Fiocruz) demonstram ação do antiviral sofosbuvir – medicamento usado no tratamento da hepatite C – em infecções por febre amarela e chikungunya. Os dados inéditos foram obtidos em testes com camundongos, considerados modelos para estudo dos agravos. Na infecção por febre amarela, o antiviral diminuiu a mortalidade e as lesões no fígado dos animais. Já nos casos de chikungunya, o sofosbuvir reduziu a mortalidade, a inflamação articular e as sequelas neurológicas. Os estudos foram liderados pelo grupo de cientistas que apontou, de foram pioneira, a ação do sofosbuvir sobre o vírus zika, em 2016. O artigo referente ao vírus da febre amarela foi divulgado no dia 30 de janeiro na revista científica Plos Neglected Infectious Diseases, enquanto o estudo sobre chikungunya foi publicado no dia 29 de janeiro na edição do periódico Antimicrobial Agentes and Chemotehrapy. Os dois estudos foram realizados em colaboração por quatro unidades da Fiocruz: Centro de Desenvolvimento Tecnológico em Saúde (CDTS), Instituto Oswaldo Cruz (IOC), Instituto Nacional de Infectologia Evandro Chagas (INI) e Instituto de Tecnologia em Fármacos (Farmanguinhos). A investigação sobre o vírus chikungunya teve ainda a cooperação com Instituto D’Or de Pesquisa (IDOR), Universidade Federal do Rio de Janeiro (UFRJ) e Consórcio BMK, formado pelas empresas Blanver Farmoquímica, Microbiológica Química e Farmacêutica e Karin Bruning. Já a pesquisa sobre o vírus da febre amarela foi feita em parceria com UFRJ e Universidade Federal de Minas Gerais (UFMG)."
frase3 = "Não envie para seus amigos."
# print(test_set_file.values.tolist())

blob = TextBlob(frase, classifier=clas)

print('Esta frase é de caráter:{}'.format(blob.classify()))
print('Precisão da previsão:{}'.format(accuracy))



