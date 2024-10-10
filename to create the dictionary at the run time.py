d={}
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    k=input("Enter the name:")
    e=int(input("Enter the marks:"))
    d[k]=e
print(d)

    
a=input("Enter the name to be searched:")
if a in d:
    print("The marks obtained:",d[a])
else :
    print("Name not found")
