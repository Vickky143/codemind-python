a=int(input())
b=int(input())
lst=[]
for i in range(a,b+1):
    prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=False
            break
    if prime==True:
        lst.append(i)
if 1 in lst:
    lst.remove(1)
for ch in lst:
    print(ch)