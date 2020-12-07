def iq_test(numbers):
    if len(numbers) == 0: 
        return None
    else:
        even = -1
        odd = -1
        numbers = numbers.split(" ")
        for i in range(0, len(numbers)):
            if int(numbers[i]) % 2 == 0: 
                if odd != -1 and even != -1:
                    return odd + 1
                even = i
            else:
                if odd != -1 and even != -1:
                    return even + 1
                odd = i
    return len(numbers)
    
