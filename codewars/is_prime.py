def isPrime(n):
    if n<=1: return False
    elif n==2 or n==3: return True
    else:
        for d in range(2, math.ceil(math.sqrt(n))+1):
            if n%d==0: return False
    return True