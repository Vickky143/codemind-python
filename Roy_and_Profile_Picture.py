n=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    if (a==n and b==n) or (a>n and b>n and a==b):
        print("ACCEPTED")
    elif (a==n and b>n) or (a>n and b==n) or (a>n and b>n):
        print("CROP IT")
    else:
        print("UPLOAD ANOTHER")