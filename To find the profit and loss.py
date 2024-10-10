c=int(input("Enter cost price:"))
s=int(input("Enter sale price:"))
if (c<s):
    p=s-c
    print("Profit:",p)
else:
    l=c-s
    print("Loss:",l)

