d={}
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    k=input("Enter the key:")
    v=int(input("Enter the value:"))
    d[k]=v
print(d)

    
a=input("Enter the key to be searched:")
if a in d:
    print("The value is:",d[a])
else :
    print("Key not found")
