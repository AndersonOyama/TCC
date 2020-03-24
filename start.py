import sys

from spellchecker import SpellChecker

def main():

    spell = SpellChecker(language='pt')

    with open('./Noticias/Falsas/Banho frio e desmaios.txt') as f:
        lines = f.read().splitlines()




    misspelled = spell.unknown(lines)

    for word in misspelled:
        spell.correction(word)
        print(word)

    pass


if __name__ == "__main__":
    main()