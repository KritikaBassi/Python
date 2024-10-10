#To delete the negative elements from the list
list1=[1,3,-5,6,-7,9,-1,4]
print(list1)
len1=len(list1)
i=0
while(i<len1):
    if (list1[i]<0):
            del list1[i]
            len1=len1-1
    i=i+1
print(list1)    

'''
l=[1,9,-8,9,2,-3,-5,7,4]
i=len(l)
i=i-1
while(i>0):
    if(l[i]<0):
        del l[i]
        
      
     
print("list after deleting:",l)

print("The list before deleting:",l)
for i in range(0,len(l)):
    a=l[i]
    if(a<0):
        l.remove(a)
    else:
        d=a
print("The list after deleting:",l)        
'''

