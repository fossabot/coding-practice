def beggars(values, n):
    beg = [0]*n
    # print(beg)
    if len(beg) > 0:
        for i in range(0, len(values)):
            beg[i%n] += values[i] # cycling through all the beggars
            # print("beg[", i%n, "] += ", values[i], "(i=", i, ")")
    return beg

def one_liner(values, n):
    """
    a list comprehension comprising the sum of every n-th element
    interesting use of step and slicing
    """
    return [sum(values[i::n]) for i in range(n)] 

print(beggars([1,2,3,4,5],3))