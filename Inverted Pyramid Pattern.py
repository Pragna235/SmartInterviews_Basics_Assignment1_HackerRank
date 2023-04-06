n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        if(i==n):
            print("* ",end="")
        else:
            if(j==0 or j==i-1):
                print("* ",end="")
            else:
                print("  ",end="")
    print()


