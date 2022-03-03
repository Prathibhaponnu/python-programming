list1=[]
list2=[]
n1=int(input("Enter the limit:"))
print("Enter integers:")
for i in range(0,n1):
   a=int(input())
   list1.append(a)
print(list1)
print("list of integers by removing even numbers:")
for i in range(0,n1):
   if(list1[i]%2!=0):
      list2.append(list1[i])
print(list2)
