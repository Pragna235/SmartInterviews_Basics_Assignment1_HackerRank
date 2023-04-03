#Given a non-negative integer - N, print the sum of digits of the given number.
n=int(input())
sum=0
while(n>0):
    sum=sum+(n%10)
    n=n//10
print(sum)
