n=int(input("Enter the step number:"))
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print(' ')
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print(' ')

