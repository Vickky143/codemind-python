a=0
b=0
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
c=len(lst1)
for i in range(c):
    if lst1[i]==lst2[i]:
        pass
    elif lst1[i]>lst2[i]:
        a+=1
    else:
        b+=1
print(a,b)