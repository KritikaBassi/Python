#To find the reverse of a number
n=int(input("Enter the number:"))
q=n
s=0
while(q>=1):
    r=q%10
    q=int(q/10)
    s=s*10+r
print("Reverse number:",s)
if(n==s):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
