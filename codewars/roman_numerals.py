import  math

def solution_andrei(n):
    """
    Create a function taking a positive integer as 
    its parameter and returning a string containing 
    the Roman Numeral representation of that integer.
    """
    if n > 3999 or n == 0:
        return None 
    
    modulus = math.pow(10,len(str(n))-1)
    roman = []
    while modulus > 0:
        if modulus == 1000:
            roman.append((int)(n//modulus) * 'M')
        if modulus == 100:
            if n//modulus < 4:
                roman.append((int)(n//modulus) * 'C')
            elif n//modulus == 4:
                roman.append('CD')
            elif n//modulus >= 5 and n//modulus < 9:
                roman.extend(['D', (int)(n//modulus-5) * 'C'])
            else: roman.append('CM')
        if modulus == 10:
            if n//modulus < 4:
                roman.append((int)(n//modulus) * 'X')
            elif n//modulus == 4:
                roman.append('XL')
            elif n//modulus >= 5 and n//modulus < 9:
                roman.extend(['L', (int)(n//modulus-5) * 'X'])
            else: roman.append('XC')
        if modulus == 1:
            if n//modulus < 4:
                roman.append((int)(n//modulus) * 'I')
            elif n//modulus == 4:
                roman.append('IV')
            elif n//modulus >= 5 and n//modulus < 9:
                roman.extend(['V', (int)(n//modulus-5) * 'I'])
            else: roman.append('IX')
        n = n % modulus
        modulus = modulus / 10
    return "".join(roman)

def solution_bestpractice(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution_andrei(4000))