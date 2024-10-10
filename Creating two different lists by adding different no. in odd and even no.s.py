l1=[]
l2=[]
l=[1,2,3,4,5,6]
print("Original list:",l)
for i in l:
    if i%2==0:
        a=i+10
        l1.append(a)
      
    else:
        b=i+5
        l2.append(b)
print("List after adding 10 in even elements:",l1)  
print("List after adding 5 in odd elements:",l2)
    
