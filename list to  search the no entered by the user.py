#To search the number entered by user
list=[1,2,3,4]
a=int(input("Enter the number to be found:"))

for i in list:
    if (a==i):
        print("The number is in list")
    if (a!=i):
        print("The number is not in list")
for i in range(0,len(list)):
    if(a==list[i]):
       print("Index:",i)
   
