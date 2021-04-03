a=input("Enter the name:")
a=list(a)
print(a)
i=0
j=1
while i<len(a):
    s=a[i]
    n=a[-j]
    j+=1
    i+=1
if s==n:
    print("It is palindrome")
else:
    print("It is not palindrome")
