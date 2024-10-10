str=input("Enter a string:")
d={}
for ch in str:
    if ch in d:
        d[ch]=d[ch]+1
    else:
        d[ch]=1
for i in d:
    print(i,":",d[i])
