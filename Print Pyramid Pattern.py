n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end = "")
    for j in range((2*i)-1):
        print("*",end = "")
    print()



