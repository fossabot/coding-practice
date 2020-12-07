import string

def spin_words(sentence):
    if len(sentence)==1: 
        return sentence
    elif len(sentence) > 1:
        return ' '.join([word if len(word.translate(str.maketrans('', '', string.punctuation))) < 5 else word[::-1] for word in sentence.split(' ')])
    return None

print(spin_words('This sentence is spun.'))
