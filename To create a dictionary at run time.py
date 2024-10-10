#To create a dictionary at run time
d={}
n=int(input("Enter the  number of elements in the dictionary:"))
for i in range (1,n+1):
    a=input("Name of the friend:")
    b=int(input("Enter the phone number:"))
    d[a]=b
print('The dictionary created is:')
print(d)
