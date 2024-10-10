'''
#Q1
c=float(input("Enter the temperature in celsius:"))
f=c*9/5+32
print("The temperature in fahrenheit:",f)

#Q2
n=int(input("Enter the number:"))
if(n%2==0):
    print("Even")
else:
    print("Odd")

#Q3
n=int(input("Enter the number:"))
if(n>0):
    print("Positive")
elif(n==0):
    print("Zero")
else:
    print("Negative")

#Q4
c=int(input("Enter the cost price:"))
s=int(input("Enter the sale price:"))
if s>c:
    p=s-c
    print("profit:",p)
else:
    l=c-s
    print("loss:",l)

#Q5
n=input("Enter the charater:")
if(n=='a' or n=='e' or n=='o' or n=='u' or n=='i'):
    print("Vowel")
else:
    print("Consonant")
   
#Q6
d=int(input("Enter the discount:"))
c=int(input("Enter the cost:"))
s=c-(c*d/100)
print("Sale price:",s)

#Q8
def rect(l,b):
    a=l*b
    p=2*(l+b)
    print("Perimeter:",p)
    print("Area:",a)

l=int(input("Enter the length:"))
b=int(input("Enter the breath:"))

rect(l,b)

#Q10
n=int(input("Enter the number:"))
a=n
while(n>1):
    n=n-1
    a=a*n
print(a)

#Q11
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#Q12
s=0
for i in range(1,101):
    s=i**2+s
print(s)


#Q13
l=int(input("Enter the limit:"))
a=0
b=1
print(a)
print(b)
for i in range (3,l+1):
    c=a+b
    a=b
    b=c
    print(c)

#Q14
n=int(input("Enter the number:"))
q=n
s=0
while(q>=1):
    r=q%10
    q=q//10
    s=r+s*10
print("Reverse:",s)

#Q15
n=int(input("Enter the number:"))
q=n
s=0
while(q>=1):
    r=q%10
    q=q//10
    s=r**3+s
if(s==n):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

#Q16
l=[]
n=int(input("Enter the number of elements to be added to the list:"))
for i in range(1,n+1):
    a=int(input("Enter the element:"))
    l.append(a)
print(l)
print("Max:",max(l))
print("Min:",min(l))


#Q17
list1=[1,3,-5,6,-7,9,-1,4]
print(list1)
len1=len(list1)
i=0
while(i<len1):
    if (list1[i]<0):
            del list1[i]
            len1=len1-1
    i=i+1
print(list1)    

'''
#Q18










