
import sys
import os
import subprocess
import random

def main():
    
    root = 'Noticias/'
    files = []
    for r, d, f in os.walk(root):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

#  for f in files:
#        print(f)

    rand = random.choices(files, k=20)
    for l in rand:
        print(l)
    pass




if __name__ == "__main__":
    main();