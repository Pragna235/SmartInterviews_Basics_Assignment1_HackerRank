n,k=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(len(l)):
    if(l[i]==k):
        flag=1
        break
if(flag==1):
    print(i)
else:
    print(-1)

