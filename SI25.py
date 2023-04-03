#Given an integer N, check whether it is a Narcissistic number or not.
#Note: A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

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


