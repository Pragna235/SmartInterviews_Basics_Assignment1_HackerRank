#Given a matrix of size N x M, print row-wise sum, separated by a newline.
#Note: Try to solve this without declaring/storing the matrix.


n,m=map(int,input().split())
for i in range(n):
    l=list(map(int,input().split()))
    print(sum(l))
