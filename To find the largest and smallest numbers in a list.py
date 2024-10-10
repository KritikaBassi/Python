#To find the largest and smallest numbers in a list
l=[]
n=int(input("Enter the number of elements:"))
for i in range (1,n+1):
    a=int(input("Enter the elements:"))
    l.extend([a])
print(l)
print("The largest number is",max(l))
print("the smallest number is",min(l))
    
