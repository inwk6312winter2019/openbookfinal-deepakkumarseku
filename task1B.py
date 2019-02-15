import string

file=open("Book1.txt")

hist = dict()
lst = []
for line in file:
    line = line.split()
    for word in line:
        word = word.strip(string.punctuation+string.whitespace).lower()
        
        hist[word] = hist.get(word,0)+1

       
print("Total number of words are %d" % sum(hist.values()))


print("Total number of different words are %d" % len(hist))

lst = [(value,key)for key,value in hist.items()]
lst.sort(reverse=True)
for item in lst[:20]:
    print(item)




