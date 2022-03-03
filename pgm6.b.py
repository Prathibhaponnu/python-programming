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
sum1=0
sum2=0
for i in list1:
    sum1=sum1+i
for i in list2:
    sum2=sum2+i
if(sum1==sum2):
    print("Both are of equal sum")
else:
    print("Both are not equal sum")


