list=[]
n=int(input("Enter number of elements in the list:"))
print("Enter the colors:")
for i in range(0,n):
    a=input()
    list.append(a)
print("list is",list)
print("First color in the list is:",list[0])
print("last color in the list is:",list[-1])
