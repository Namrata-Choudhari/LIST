a=[10,20,30,40,10,20,30,40,50,60,10]
i=0
j=1
while i<len(a)/2:
    s=a[i]
    print(s)
    n=a[-j]
    print(n)
    if s==n:
        print("They are equal")
    else:
        print("They are not equal")
    j=j+2
    i=i+2


