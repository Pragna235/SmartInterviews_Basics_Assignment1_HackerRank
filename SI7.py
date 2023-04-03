#Given a matrix of size N x M, print column-wise sum, separated by a newline.

n,m=map(int,input().split())
arr=[0 for i in range(m)]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(len(l)):
        arr[j]=l[j]+arr[j]
for ele in arr:
    print(ele)



