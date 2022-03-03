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
for x in list1:
    if(x in list1 and x in list2):
        print(x)
