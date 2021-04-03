a=[10,11,12,13,14,17,18,19]
i=1
h=[]
while i<len(a)/2:
    s=a[i]
    j=1
    while j<len(a):
        n=a[j]
        if s+n==30:
            h.append([s,n])
        j=j+1
    i=i+1
print(h)