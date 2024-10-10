l=[]
n=int(input("How many numbers do you  want to enter:"))
'''for i in range(0,n):
    a=int(input("Enter the element:"))
    l.append(a)
print(l)'''
i=0
while (i<n):
    a=int(input("Enter the element:"))
    l.append(a)
    i=i+1
print(l)
s=int(input("Enter the element to be searched:"))
if (s in l):
    d=l.index(s)
    print(s,"is at index",d)
else:
    print("Element not found")
    
