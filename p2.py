def compare(s1, s2, n):
    for i in range(n):
        if s1[0:n] == s2[0:n]:
            return True
        else:
            return False


string1 = input("Enter the string1:")
string2 = input("Enter the string2:")
n = int(input("Enter the value of n:"))
print(compare(string1, string2, n))
