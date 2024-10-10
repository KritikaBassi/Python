#Using functions find the area,perimeter of rect,square,triangle,circle
def rect(l,b):
    a1=l*b
    p1=2*(l+b)
    print('Area:',a1)
    print('Perimeter:',p1)
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
rect(l,b)

def square(s):
    a2=s*s
    p2=4*s
    print("Area:",a2)
    print("Perimeter:",p2)
s=int(input("Enter side of square:"))
square(s)

def triangle(l1,l2,l3,h):
    a3=l2*h/2
    p3=l1+l2+l3
    print("Area:",a3)
    print("Perimeter:",p3)
l1=int(input("Enter the first length:"))    
l2=int(input("Enter the second length:"))
l3=int(input("Enter the third length:"))
h=int(input("Enter height:"))
triangle(l1,l2,l3,h)

def circle(r):
    a4=22/7*r**2
    p4=2*22/7*r
    print("Area:",a4)
    print("Perimeter:",p4)
r=int(input("Enter the radius:"))
circle(r)
