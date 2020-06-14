import re

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from spellchecker import SpellChecker
from googletrans import Translator



def multi_replace(reg, text):
    regex = re.compile("|".join(map(re.escape, reg.keys(  ))))
    return regex.sub(lambda match: reg[match.group(0)], text)

def countSpellError(file):
    translator = Translator()
    spell = SpellChecker(language=None, local_dictionary="./dictionary/fused_compiles.txt")
    

# CRIAR DICIONARIO E "COMPILAR" ELE PARA USO DO SPELLCHECKER 

    # spell = SpellChecker(language=None)
    # spell.word_frequency.load_text_file("./dictionary/fused.txt")
    # spell.export("./dictionary/fused_compiles.txt")

    lines = []

    reg = {
        "." : "",
        "," : "",
        "’" : "",
        "-" : " ",
        "?" : "",
        "!" : "",
        "%" : "",
        "\"" : "",
        "\'" : "",
        "\“" : "",
        "\“" : "",
        "/" : " ",
        "”" : "",
        "*" : "",
        "–" : ""
    }


    with open(file, 'r') as f:
        lines = word_tokenize( multi_replace(reg, re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}     /)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', f.read().lower(), flags=re.MULTILINE)))

    misspelled = spell.unknown(lines)
    # try:
    translated = translator.translate(TreebankWordDetokenizer().detokenize(misspelled), dest = 'en', src = 'pt')
    #     print(translated.text, "\n", misspelled, "\n")
    #     error_translated = translator.translate
    #     print(TreebankWordDetokenizer().detokenize(error_translated))
    #     # new_errors = spell.unknown
    # except Exception as e:
    #     print(str(e))
        


    # for word in misspelled:
        # spell.correction(word)
        # print(word)
        # print(word, spell.correction(word))
        # nmberOfError += 1
    
    count = (len(misspelled)/len(lines))

    return misspelled, count



def main():

    spell = SpellChecker(language=None)
    spell.word_frequency.load_text_file("./dictionary/ime.txt")
    spell.export("./dictionary/dictionary_compiled_ime.txt")

    exit(0)

    if __name__ == '__main__':
        main()
        
