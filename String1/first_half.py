# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    str2 = str[:len(str) // 2]
    return str2
