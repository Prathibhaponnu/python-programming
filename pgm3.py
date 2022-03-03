snt=input("Enter the sentence:")
splitsnt=snt.split()
setsnt=set(splitsnt)
dict={}
for i in setsnt:
    x=snt.count(i)
    dict.update({i:x})
print(dict)

