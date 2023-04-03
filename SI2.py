#Print unique elements of the array in the same order as they appear in the input.
Note: Do not use any inbuilt functions/libraries for your main logic.
n=int(input())
l=list(map(int,input().split()))
#unique=l[0]
for ele in l:
    if(l.count(ele)==1):
        print(ele,end=" ")


