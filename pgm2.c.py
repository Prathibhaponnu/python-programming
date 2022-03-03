word=input("Enter any word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
list=[]
for x in word:
    if(x in vowels and x not in list):
        list.append(x)
print("Vowels present in given word",list)
