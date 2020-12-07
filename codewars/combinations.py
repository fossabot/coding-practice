def fac(n):
    print("n=", n)
    if n==1: 
        return n
    else:
        return n*fac(n-1)
    
def choose(n, k):
    print("n= ", n, "k=", k)
    if n < 0 or k < 0 or n < k:
        return 0
    if n == k:
        return 1
    if k < n-k:
        k = n-k
    temp = k+1
    p = temp
    while temp < n:
        temp = temp + 1
        p = p * temp
    return p//fac(n-k)

print(choose(1215, 29))