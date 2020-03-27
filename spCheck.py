import re

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

def countSpellError(file):
    nmberOfError = 0

    spell = SpellChecker(language='pt')
    lines = []

    with open(file, 'r') as f:
        lines = word_tokenize(f.read())
    misspelled = spell.unknown(lines)

    for word in misspelled:
        # spell.correction(word)
        # print(word)
        # print(word, spell.correction(word))
        nmberOfError += 1
    
    count = (nmberOfError/len(lines))

    return misspelled, count
