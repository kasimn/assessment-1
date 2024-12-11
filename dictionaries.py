file = open("textfile.txt")
words = file.readlines()[0].split(",")
print(words)
file.close()
dct = {}

for word in words:
    print(word)
    dct[word] = dct.get(word,0) + 1
    print(dct)
    
