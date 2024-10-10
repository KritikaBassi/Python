#delete the value from dict that is inputed by the user
d={'A':85,'B':95,'C':88,'D':90,'E':75}
n=input("Enter a name:")
if n in d:
    d.pop(n)
else:
    print("Name not found")
print("Dictionary after deletion:")
print(d)
