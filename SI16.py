#Find the missing number in the given list of integers. The list contains 1 to 100 integers but one of the integer is missing. There are no duplicates in the list.
l=list(map(int,input().split()))
print(5050-sum(l))
