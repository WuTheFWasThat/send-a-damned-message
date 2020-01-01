alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_vowel(l):
    return l.lower() in 'aeiou'

def is_consonant(l):
    return l.lower() in 'bcdfghjklmnpqrstvwxyz'

def a2num(x):
    return ord(x.lower()) - ord('a')

def num2a(n):
    return chr(n + ord('a'))

def is_alphabet(l):
    return l.lower() in alphabet

def rotate_alphabet(x, direction):
    is_upper = x == x.upper()
    new_x = num2a((a2num(x) + direction) % 26)
    if is_upper:
        new_x = new_x.upper()
    return new_x
