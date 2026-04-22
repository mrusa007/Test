n=int(input("enter a number of terms:"))
a= 0
b= 1
print("fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    c= a + b
    a= b
    b=c
