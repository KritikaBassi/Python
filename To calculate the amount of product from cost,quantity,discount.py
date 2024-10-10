#To calculate the amount of product from cost,quantity,discount
c=float(input("Enter the cost:"))
q=int(input("Enter the quantity:"))
d=int(input("Enter the discount offered:"))
a=c*q-(c*q*d/100)
print("Amount of product:",a)
