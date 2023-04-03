#Given an integer N, check whether it is a Harshad number or not.
#Note: A Harshad number is an integer, that is divisible by the sum of its digits.

n=int(input())
m,sum=n,0
while(m>0):
    sum=sum+(m%10)
    m=m//10
if(n%sum==0):
    print("Yes")
else:
    print("No")
