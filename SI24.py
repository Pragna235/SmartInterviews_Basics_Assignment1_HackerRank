#Given an integer N, check whether it's an Armstrong number or not.
#Note: Armstrong number is a number that is equal to the sum of cubes of its digits.

n=int(input())
nod=len(str(n))
m,sum=n,0
while(m>0):
    sum=sum+((m%10)**nod)
    m=m//10
if(sum==n):
    print("Yes")
else:
    print("No")

