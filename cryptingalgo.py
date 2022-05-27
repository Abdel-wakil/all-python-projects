def atbash(txt):
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',' ', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    final_letters=[]

    for i in txt:
        index_0=alphabets.index(i)
        index_f=26-index_0
        final_letters+=[alphabets[index_f]]

    return("".join(final_letters))




