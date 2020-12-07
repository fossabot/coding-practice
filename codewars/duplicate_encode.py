def duplicate_encode(word):
    word = word.lower()
    return "".join(['(' if word.count(a)==1 else ')' for a in word])