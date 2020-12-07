import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]+", "", string)

print(disemvowel("This is a string."))