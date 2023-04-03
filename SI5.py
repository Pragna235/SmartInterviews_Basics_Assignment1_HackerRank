#Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
#Note: Do not use any inbuilt functions/libraries for your main logic.


n=int(input())
l=list(map(int,input().split()))
for ele in l:
    if(l.count(ele)==2):
        print(ele)
        break
