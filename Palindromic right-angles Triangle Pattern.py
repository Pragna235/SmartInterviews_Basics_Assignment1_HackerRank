n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+65-1),end=" ")
    for k in range(i-1,0,-1):
        print(chr(k+65-1),end=" ")
    print()



