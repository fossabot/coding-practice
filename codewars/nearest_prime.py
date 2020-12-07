import math

def isPrime(n):
    if n==1: return False
    elif n==2 or n==3: return True
    else:
        for d in range(2, math.ceil(math.sqrt(n))+1):
            if n%d==0: return False
    return True

def solve(n):
    if n==0: return 0
    if isPrime(n): return n
    else:
        if n%2==0: 
            i = 1
        else:
            i = 2
        while True:
            if isPrime(n-i):
                return n-i
            if isPrime(n+i):
                return n+i
            i = i + 2