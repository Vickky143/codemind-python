a=int(input())
lst=list(map(int,input().split()))
m=sum(lst)
if m%2==0:
    print("1")
else:
    print("0")