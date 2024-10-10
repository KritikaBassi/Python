#to remove if name is found else add it at index 2
l=['a','b','c','d','e']
n=input("Enter the name:")
if n in l:
    l.remove(n)
else:
    l.insert(2,n)
print(l)    
