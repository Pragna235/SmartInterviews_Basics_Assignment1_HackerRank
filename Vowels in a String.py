s=input()
flag=0
l=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if(i not in l):
        flag=1
        break
if(flag==1):
    print("No")
else:
    print("Yes")N
