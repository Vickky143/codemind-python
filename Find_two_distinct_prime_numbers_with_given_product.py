n=int(input())
a=[]
count=0
for i in range(2,n):
    if n%i==0:
        a.append(i)
v=1
b=[]
for ch in a:
    for j in range(2,int(ch**0.5)+1):
        if ch%j==0:
            v=2
            break
    if v==1:
        count+=1
        b.append(ch)
if count>=2:
    for d in b:
        print(d,end=' ')
else:
    print('-1')