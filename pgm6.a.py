list1=[]
list2=[]
n1=int(input("Enter the number of elements in list1:"))
n2=int(input("Enter the number of elements of list2:"))
print("Enter integers in list1:")
for i in range(0,n1):
    a=int(input())
    list1.append(a)
print(list1)
print("Enter integers in list2: ")
for i in range(0,n2):
    b=int(input())
    list2.append(b)
print(list2)
len1=len(list1)
len2=len(list2)
if(len1==len2):
    print("Same length")
else:
    print("Not same length")
