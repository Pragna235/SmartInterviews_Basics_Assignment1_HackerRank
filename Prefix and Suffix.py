def lpres(string):
    n=len(string)
    lps=[0]*n
    
    length=0
    
    i=1
    while(i<n):
        if(string[i] == string[length]):
            length+=1
            lps[i]=length
            i+=1
        else:
            if(length!=0):
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps[-1]

input=input()
print(lpres(input))
