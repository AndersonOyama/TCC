import os
import sys
import random
import xlsxwriter

def list_files(dir):
    return (f for f in os.listdir(dir) if f.endswith('.'+"txt"))

def main(dir, tam):
    files = list_files(dir)
    files = list(files)
    files.sort()

    results = xlsxwriter.Workbook("/home/anderson/Documentos/aleatorio/sensa/test_gen_sensa.xlsx")
    worksheet = results.add_worksheet()

    row = 0
    column = 0

    print(len(files))


    print("\n".join(files))
    for f in files:
        with open(dir+f, 'r') as f:   
            worksheet.write(row, column, f.read())
            worksheet.write(row, column+1, "")
            row +=1
            f.close()


    results.close()

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2])) 