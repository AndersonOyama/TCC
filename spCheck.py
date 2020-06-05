import re

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker



def multi_replace(reg, text):
    regex = re.compile("|".join(map(re.escape, reg.keys(  ))))
    return regex.sub(lambda match: reg[match.group(0)], text)

def countSpellError(file):
    spell = SpellChecker(language=None, local_dictionary="./dictionary/dictionary_compiled.txt")

# CRIAR DICIONARIO E "COMPILAR" ELE PARA USO DO SPELLCHECKER 

    # spell = SpellChecker(language=None)
    # spell.word_frequency.load_text_file("./dictionary/ime.txt")
    # spell.export("./dictionary/dictionary_compiled_ime.txt")

    lines = []

    reg = {
        "." : "",
        "," : "",
        "-" : " ",
        "?" : "",
        "!" : "",
        "%" : "",
        "\"" : "",
        "\'" : "",
        "\“" : "",
        "/" : " ",
        "”" : "",
        "*" : ""
    }

    with open(file, 'r') as f:
        lines = word_tokenize( multi_replace(reg, re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}     /)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', f.read().lower(), flags=re.MULTILINE)))
    misspelled = spell.unknown(lines)

    # for word in misspelled:
        # spell.correction(word)
        # print(word)
        # print(word, spell.correction(word))
        # nmberOfError += 1
    
    count = (len(misspelled)/len(lines))

    return misspelled, count