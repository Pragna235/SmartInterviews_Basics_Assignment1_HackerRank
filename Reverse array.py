#Print array in reverse order.
#Note: Try solving this using recursion. Do not use any inbuilt functions/libraries for your main logic.

n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    print(l[n-i-1],end=" ")
