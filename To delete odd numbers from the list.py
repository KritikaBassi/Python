#To delete odd numbers from the list
l=[1,2,3,4,5]
for i in l:
    if i%2 != 0:
        l.remove(i)
print("List after deleting:",l)        
        
