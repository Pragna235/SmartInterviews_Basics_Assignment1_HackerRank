n = int(input())
s = 1
for i in range(n):
    for j in range(n,0,-1):
        if j == s :
            print('*',end = '')
        else:
            print(j,end = '')
    s += 1
    print()

