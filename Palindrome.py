n=int(input())
t=n
x=0
while n>0:
    r=n%10
    x=(x*10+r)
    n=n//10
if t==x:
    print("True")
else:
    print("False")
    