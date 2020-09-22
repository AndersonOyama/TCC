import os
import sys
import random
import xlsxwriter

def list_files(dir):
    return (f for f in os.listdir(dir) if f.endswith('.'+"txt"))

def main(dir, tam):
    files = list_files(dir)
    files = list(files)

    results = xlsxwriter.Workbook("train_gen.xlsx")
    worksheet = results.add_worksheet()

    row = 0
    column = 0

    print(files, len(files))


    list_f = random.choices(files, k=tam)
    print(list_f)
    for f in list_f:
        with open(dir+f, 'r') as f:   
            worksheet.write(row, column, f.read())
            row +=1
            f.close()


    results.close()
    
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))