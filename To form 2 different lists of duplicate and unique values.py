#To form 2 different lists of duplicate and unique values
l=[1,2,3,2,3,5,6,4,8,5]
l1=[]
l2=[]
for i in l:
    a=l.count(i)
    if a>1:
        l1.append(i)
    if a==1:
        l2.append(i)
        
print("List formed by duplicate values:",l1)
print("List formed by unique values:",l2)
