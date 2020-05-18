import sys
import os
import xlsxwriter
import string

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from array import array
from os import listdir
from spCheck import countSpellError

def list_files(dir):
    return (f for f in os.listdir(dir) if f.endswith('.'+"txt"))

def listToString(s):
    string = ""
    for a in s:
        string += a
    return string

def main(dir):
    files = list_files(dir)
    files = list(files)
    files.sort()
    

    results = xlsxwriter.Workbook("resultados.xlsx")
    worksheet = results.add_worksheet()

    percent_fmt = results.add_format({'num_format': '0.00%'})
    # cell_format = results.add_format()
    # cell_format.set_text_wrap()

    row = 1
    column = 0

    worksheet.write(0, 0, 'Texto')
    worksheet.set_column(0, 0, 50)

    worksheet.write(0, 1, 'Palavras erradas')
    worksheet.set_column(1, 1, 100)

    worksheet.write(0, 2, 'Porcentagem de erro ortográfico')
    worksheet.set_column(2, 2, 30, percent_fmt)

    worksheet.write(0, 3, 'Quantidade de palavras')
    worksheet.set_column(3, 3, 100)

    worksheet.write(0, 4, 'Quantidade de paragrafos')
    worksheet.set_column(4, 4, 80)

    worksheet.write(0, 5, 'Solicita compartilhamento?')
    worksheet.set_column(5, 5, 60)

    

    for i in files:
        worksheet.write(row, column, i)
        row += 1

    row = 1
    column += 1
    
    for f in files:
        corretor = countSpellError(dir+'/'+f)
        worksheet.write(row, column, ', '.join(corretor[0]))
        worksheet.write(row, column+1, corretor[1])
        row += 1
       


    results.close()
    pass





if __name__ == "__main__":
    main(sys.argv[1])