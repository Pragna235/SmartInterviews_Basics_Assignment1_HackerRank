#Print sum of all odd elements in an array.
n=int(input())
l=list(map(int,input().split()))
sum=0
for ele in l:
    if(ele%2!=0):
        sum=sum+ele
print(sum)
