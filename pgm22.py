list=[]
n=int(input("Enter the limit:"))
print("Enter the items:")
for i in range (n):
    num=int(input())
    list.append(num)
print("Sum of elements in given list is:",sum(list))
