n=int(input())
m=list(map(int,input().split()))
for ch in range(len(m)):
    if m[ch]%2==0:
        v=ch
print(v)