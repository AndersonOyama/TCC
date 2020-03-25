import re

from spellchecker import SpellChecker

def countSpellError(file):

    spell = SpellChecker(language='pt')
    lines = []
    with open(file, 'r') as f:
        lines = [word.replace('.', '').replace(',','') for line in f for word in line.split()]
    f.close()
    count = 0
    misspelled = spell.unknown(lines)

    for word in misspelled:
        # spell.correction(word)
        # print(word)
        # print(word, spell.correction(word))
        count += 1
    
    
    return misspelled, count
