n=int(input())
v=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        v=2
        break
if v==1:
    print('prime')
else:
    print('not a prime')