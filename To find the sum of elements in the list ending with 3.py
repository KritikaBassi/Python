#To find the sum of elements in the list ending with 3
l=[12,23,34,33,35,67,83]
s=0
for i in l:
    if i%10==3:
        s=s+i
print("Sum:",s)    
