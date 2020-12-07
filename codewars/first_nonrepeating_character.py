def first_non_repeating_letter(string):
    if len(string) > 0:
        types = dict.fromkeys(string)
        lowercase = string.lower()
        print("typ=", types)
        for l in types:
            print("l=", l)
            if lowercase.count(l.lower()) == 1:
                return l
    return ''

print(first_non_repeating_letter("stress"))
