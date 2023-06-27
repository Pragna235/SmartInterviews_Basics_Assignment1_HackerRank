$#Given a positive integer - N, print the number of multiples of 3, 5 between [1, N].
n=int(input())
print(n//3+n//5-n//15)
