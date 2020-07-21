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

    spell = SpellChecker(language=None, local_dictionary="./dictionary/dictionary_usp_libre_office_fused_compiled.txt")
    

# CRIAR DICIONARIO E "COMPILA" ELE PARA USO DO SPELLCHECKER 

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
    # translated = translator.translate(TreebankWordDetokenizer().detokenize(misspelled), dest = 'en', src = 'pt')
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
    
    count_errors = (len(misspelled)/len(lines))
    paragraph = (len(lines.paras()))

    return misspelled, count_errors, paragraph



def main():

    spell = SpellChecker(language=None)
    spell.word_frequency.load_text_file("./dictionary/dictionary_usp_libre_office_fused.txt")
    spell.export("./dictionary/dictionary_usp_libre_office_fused_compiled.txt")

  

if __name__ == '__main__':
        main()
        
