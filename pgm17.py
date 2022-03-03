import operator
d1 = {}
n = int(input("size of dictionary1"))
print("Enter data :")
for i in range(0,n,1):
   key = input("key : ")
   value = input("value : ")
   d1.update({key : value})
print("dictionary1 is ",d1)
import operator
d2 = {}
n = int(input("size of dictionary2"))
print("Enter data :")
for i in range(0,n,1):
   key = input("key : ")
   value = input("value : ")
   d2.update({key : value})
print("dictionary2 is",d2)
def merge(d1,d2):
 return (d1|d2)
print("merged dictionary")
print(merge(d1,d2))
