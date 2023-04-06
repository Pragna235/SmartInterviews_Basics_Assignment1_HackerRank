s=input()
i=0
empty=""
length=len(s)
while(i!=length):
    count=1
    while((i<length-1) and (s[i] == s[i+1])):
        count+=1
        i+=1
    empty=empty+str(s[i])+str(count)
    i+=1
print(empty)


