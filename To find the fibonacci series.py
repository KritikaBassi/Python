#To find the fibonacci series
n=int(input("Enter the limit:"))
a=0
b=1
print("Fibonacci Series is:")
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c)
