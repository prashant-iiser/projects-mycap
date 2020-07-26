import operator
word=input("enter a word: ")

alphabet= {}

for i in word:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1
        
sorted_alphabet= dict(sorted(alphabet.items(),key=operator.itemgetter(1),reverse=True))

print(str(sorted_alphabet))
