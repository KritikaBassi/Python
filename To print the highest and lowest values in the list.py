#To print the highest and lowest values in the list input by user
l=[]
a=int(input("Enter the number of total elements in the list:"))
for i in range(0,a):
    n=int(input("Enter the element:"))
    l.append(n)
print("The list formed is:",l) 
print("The largest number is:",max(l))
print("The smallest number is:",min(l))
