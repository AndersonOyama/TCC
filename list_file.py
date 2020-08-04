
import sys
import os
import subprocess

def main():
    
    root = 'Noticias/'
    files = []
    for r, d, f in os.walk(root):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)

    pass




if __name__ == "__main__":
    main();