#Create a dictionary to store names of states and capitals

d={}
n=int(input("Enter the number of elements to be added:"))
for i in range (1,n+1):
    k=input("Enter the state:")
    v=input("Enter the capital:")
    d[k]=v
    
print(d)
