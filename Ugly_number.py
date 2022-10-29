a=int(input())
k=[]
for i in range(1,a+1):
    if a%i==0:
        k.append(i)
if 2 in k or 3 in k or 5 in k:
    print("Ugly Number")
elif a==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")