#For a given positive integer - N, compute Nth fibonacci number.
def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(int(input())))
