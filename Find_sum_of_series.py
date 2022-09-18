n=int(input())
sum=0
for i in range(1,n+1):
    i=1/i
    sum=sum+i
print('{:.2f}'.format(sum))