import re

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

def countSpellError(file):
    nmberOfError = 0

    spell = SpellChecker(language=None, local_dictionary="./language/asfd.txt")

    # spell = SpellChecker(language=None)
    # spell.word_frequency.load_text_file("./language/pt_br_full_ignored_en.txt")
    # spell.export("./language/dictionary_compiled.txt")

    lines = []

    with open(file, 'r') as f:
        lines = word_tokenize( re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}     /)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '',f.read(), flags=re.MULTILINE))
    misspelled = spell.unknown(lines)

    for word in misspelled:
        # spell.correction(word)
        # print(word)
        # print(word, spell.correction(word))
        nmberOfError += 1
    
    count = (nmberOfError/len(lines))

    return misspelled, count
