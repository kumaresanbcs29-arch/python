sentence=input("enter a sentence:")
words=sentence.split()
unique=[]
for word in words:
    if word not in unique:
        unique.append(word)
print("unique words:",unique)
print("number of unique words:",len(unique))
