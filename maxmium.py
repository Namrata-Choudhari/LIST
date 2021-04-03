a=[50,40,120,23,70,56,12,5,10,7]
i=0
max=a[i]
while i<len(a):
    if max<a[i]:
        max=a[i]
    i+=1
print(max)