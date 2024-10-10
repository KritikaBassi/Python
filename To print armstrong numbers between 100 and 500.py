#To print armstrong numbers between 100 and 500
for n in range (100,501):
    a=n%10
    b=n//10
    d=b%10
    c=n//100
    if (a**3+d**3+c**3==n):
        print(n)
    
'''
#To check whether the number entered by the user is an armstrong number
n=int(input("Enter a number:"))
a=n
s=0
while (n>0):
    r=n%10
    s=s+r**3
    n=n//10
if(s==a):
    print(a," is an armstrong number")
else:
    print(a," is not an armstrong number")
'''
    
