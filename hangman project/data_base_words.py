import os,sys


with open(os.path.join(sys.path[0], "data_base_word.txt"), "r") as f:
    print(f.read())