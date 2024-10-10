l=["Khushi","Prisha","Ritika","Aastha","Harshita"]
print(l)
n=input("Enter the name to be added:")
l.append(n)
print("New list:",l)
'''a=input("Enter the index:")
if a in range(0,len(l)):
    print("Name at the index:",l[b])
else:
    print("Error")'''
list2=['Kamal','Sanjana']
g=list2+l
print('New list:',g)
d=input("Enter a name:")
if d not in l:
    l.append(d)
    print("New list:",l)
else:
    print("Name already exists in the list")
list3=l
list3.reverse()
print("Reverse list:",list3)
l.pop()
print("New list:",l)
list5=[2,5,-4,-5,3,-6,8]


    
    
