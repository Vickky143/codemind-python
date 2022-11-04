n=int(input())
m=list(str(n))
for i in range(len(m)):
    if m[i]=='6':
        m[i]='9'
        break
for i in m:
    print(i,end='')
