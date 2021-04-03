a=[1,0,0,1,1]
i=1
b=[]
while i<=len(a):
    b.append(a[-i])
    i=i+1
print(b)
x=0
sum=0
while x<len(b):
    if b[x]==1:
        sum+=2**x
    x+=1
print(sum)