s=input()
c1,c2=0,0
l=['a','e','o','i','u','A','E','I','O',"U"]
for i in s:
    if(i in l):
        c1+=1
    else:
        c2+=1
print(c1,c2)
