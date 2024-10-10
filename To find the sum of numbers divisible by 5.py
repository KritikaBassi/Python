#To find the sum of numbers divisible by 5
l=[1,23,5,45,36,58,75]
s=0
for i in l:
    if i%5==0:
        s=s+i
print("The sum of number divisible by 5 is:",s)        
