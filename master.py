import sys
import os
import xlsxwriter

from array import array
from start import countSpellError

def main(dir):
    files = os.listdir(dir)
    results = xlsxwriter.Workbook("resultados.xlsx")
    worksheet = results.add_worksheet()

    row = 1
    column = 0

    worksheet.write(0, 0, 'Texto')
    worksheet.write(0, 1, 'Palavras erradas')
    worksheet.write(0, 2, 'Porcentagem de erro ortográfico')

    for i in files:
        worksheet.write(row, column, i)
        row += 1

    row = 1
    column += 1
    
    for f in files:
        corretor = countSpellError(dir+'/'+f)
        worksheet.write(row, column, listToString(corretor[0]))
        worksheet.write(row, column+1, corretor[1])
        row += 1
       




    results.close()
    pass


def listToString(s):
    string =""
    for a in s:
        string += a
    return string


if __name__ == "__main__":
    main(sys.argv[1])