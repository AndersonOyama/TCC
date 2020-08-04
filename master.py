import sys
import os
import xlsxwriter
import string

# /home/anderson/Documentos/Github/TCC/Noticias/Falsas

from array import array
from os import listdir
from spCheck import countSpellError
from share import shareCheck
from sensacionalistaChecker import sansaChecker
from jpype import *

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
    worksheet.set_column(3, 3, 25)

    worksheet.write(0, 4, 'Quantidade de parágrafos')
    worksheet.set_column(4, 4, 25)

    worksheet.write(0, 5, 'Solicita compartilhamento?')
    worksheet.set_column(5, 5, 25)

    worksheet.write(0, 6, 'Compartilhamento valorado')
    worksheet.set_column(6, 6, 30)

    worksheet.write(0, 7, 'Notícia sensacionalista?')
    worksheet.set_column(7, 7, 20)

    worksheet.write(0, 8, 'Sensacionalismo valorado')
    worksheet.set_column(8, 8, 30)

    worksheet.write(0, 9, 'Resultado final')
    worksheet.set_column(9, 9, 30)

    worksheet.write(0, 10, 'Deffuzy')
    worksheet.set_column(10, 10, 20)    

    for i in files:
        worksheet.write(row, column, i)
        row += 1

    row = 1
    column += 1
    

    # VERIFICADOR DE ERROS GRAMÁTICAIS
    for f in files:
        corretor = countSpellError(dir+'/'+f)
        worksheet.write(row, column, ', '.join(corretor[0]))
        worksheet.write(row, column+1, corretor[1])
        row += 1
       
    #VERIFICADOR DE SOLICITAÇÃO DE COMPARTILHAMENTO
    column += 4

    compartilhamento, accuracy = shareCheck(files, dir)
    compartilhamento_value = []

    for i in range(0, len(compartilhamento), 1):
        if( compartilhamento[i] == 'compartilhamento'):
            compartilhamento_value.append(accuracy*(-1))
        else:
            compartilhamento_value.append(accuracy*1)

    for i in range(0, len(compartilhamento), 1):
        worksheet.write(i+1, column, compartilhamento[i])
        worksheet.write(i+1, column+1, compartilhamento_value[i])
    worksheet.write(len(compartilhamento) + 1, column, "Acurácia: " + str((accuracy*100)) + "%")

    #VERIFICADOR DE SENSACIONALISMO

    column += 2

    sensacionalista, accuracy = sansaChecker(files, dir)
    sensacionalista_value = []

    for i in range(0, len(sensacionalista), 1):
        if( sensacionalista[i] == 'não sensacionalista'):
            sensacionalista_value.append(accuracy*1)
        else:
            sensacionalista_value.append(accuracy*(-1))

    for i in range(0, len(sensacionalista), 1):
        worksheet.write(i+1, column, sensacionalista[i])
        worksheet.write(i+1, column+1, sensacionalista_value[i])
    worksheet.write(len(sensacionalista) + 1 , column, "Acurácia: " + str((accuracy*100)) + "%")


    results.close()


    return 0





if __name__ == "__main__":
    main(sys.argv[1])