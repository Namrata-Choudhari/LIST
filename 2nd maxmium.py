a=[50,40,23,120,70,80,56,12,5,10,7]
i=0
j=0
max1=a[i]
max2=a[j]
while i<len(a):
    if max1<a[i]:
        max1=a[i]
    i=i+1
a.remove(max1)
while j<len(a):
    if max2<a[j]:
        max2=a[j]
    j=j+1
print(max2)
