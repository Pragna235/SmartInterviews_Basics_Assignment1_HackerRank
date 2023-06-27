#Given the length of 3 sides of a triangle, check whether the triangle is valid or not.
a,b,c=map(int,input().split())
if(((a+b)<= c) or ((b+c) <= a) or ((c+a) <= b)):
    print("No")
else:
    print("Yes")
