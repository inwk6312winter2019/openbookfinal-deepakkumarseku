import string 

file=open("Book1.txt")
hist = dict()
for line in file:
    line = line.split()
   	for word in line:
            word = word.strip(string.punctuation+string.whitespace).lower()
        	
         	hist[word] = hist.get(word,0)+1

def unique_words():
  	print("Total number of words are %d" % sum(hist.values()))
	print("Total number of different words are %d" % len(hist))
	for key,value in hist.items():
    	print(key,value,sep ='\t')
unique_words()


def count_the_article():
 
 count = 0
    list = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    if words in list:
        count[words] += 1
    else:
        count[words] = 1
 for word, times in count.items():
    print ("%s :  %d times" % (word, times))
count_the_article()


def  sorted_words():
file=open("Book1.txt")
hist = dict()
for line in file:
    line = line.split()
        for word in line:
            word = word.strip(string.punctuation+string.whitespace).lower()
	words.sort()

# display the sorted words

	print("The sorted words are:")
	for word in words:
   	print(word)
sorted_words()

def charecter_word_count():
 hist = dict()
    file = open("Book1.txt")
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = len(word)
    return hist


def starts_with_vowel():
file=open("Book1.txt")
hist = dict()
for line in file:
    line = line.split()
        for word in line:
            word = word.strip(string.punctuation+string.whitespace).lower()
            word.lower()
   		index = 0
   		vowelSet = set(['a','e','i','o','u'])
   		vowels = 0
   		consonants = 0
    		while index < len(line):
        		if line[index] in vowels:
            		vowels += 1
            		index += 1
        print('This string consists of ' + word(vowels) + 'vowels')
starts _with_vowel()
