import math

def isPrime(n):
    if n==1: return False
    elif n==2 or n==3: return True
    else:
        for d in range(2, math.ceil(math.sqrt(n))+1):
            if n%d==0: return False
    return True

def prime_divisors(n):
    return [d for d in range(2, n+1) if isPrime(d) and n%d==0]

def sum_for_list(lst):
    primes = {}
    if len(lst) <= 0:
        return []
    for num in lst:
        print("num=", num)
        if isPrime(math.fabs(num)) and (int)(math.fabs(num)) not in primes:
            print("first push prime [", (int)(math.fabs(num)), "] =", (int)(math.fabs(num)))
            primes[(int)(math.fabs(num))] =  num
        else:
            for prime_div in prime_divisors((int)(math.fabs(num))):
                if prime_div in primes:
                    print("adding [", prime_div, "] =", primes[prime_div] + num)
                    primes[prime_div] = primes[prime_div] + num
                else:
                    print("first push  [", prime_div, "] =", num)
                    primes[prime_div] = num
    prim_li =  list(map(list, primes.items()))
    prim_li.sort()
    return prim_li

def sum_for_list_short(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]
    
print(sum_for_list([-152, -19, -114]))