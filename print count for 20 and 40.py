a=[50,40,23,70,56,12,5,10,7]
i=0
count_20=0
count_40=0
while i<len(a):
    count=a[i]
    if count>20:
        count_20=count_20+1
    else:
        count_40=count_40+1
    i+=1
print(count_20)
print(count_40)