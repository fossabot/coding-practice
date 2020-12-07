def make_readable(seconds):
    if seconds > 359999:
        return None

    readable = ""

    if seconds >= 3600:
        if seconds//3600 > 9:
            readable = readable + (str)(seconds//3600)
        elif seconds//3600 <= 9 and seconds//3600 > 0: 
            readable = readable + "0" + (str)(seconds//3600)
        seconds = seconds%3600
    else:
        readable = readable + "00"
    # print("After hour mark: ", seconds)
    if seconds >= 60:
        if seconds//60 > 9:
            readable = readable + ":" + (str)(seconds//60)
        elif seconds//60 <= 9 and seconds//60 > 0: 
            readable = readable + ":0" + (str)(seconds//60)
        seconds =  seconds%60
    else:
        readable = readable + ":00"
    # print("After minute mark: ", seconds)
    if seconds > 0:
        if seconds > 9:
            readable = readable + ":" + (str)(seconds)
        else:
            readable = readable + ":0" + (str)(seconds)
    else:
        readable = readable + ":00"
    return readable

def make_readable_bestpractice(seconds):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)