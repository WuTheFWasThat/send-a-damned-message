from utils import is_consonant

def reflect(x):
    for i, char in enumerate(x):
        if is_consonant(char):
            return reflect(x[i+1:][::-1]) + char + x[:i][::-1]
    return x

if 0:
    # verify the cycle is long
    all_ms = set()
    cur = 'a damned message'
    while True:
        print(cur)
        if cur in all_ms:
            break
        all_ms.add(cur)
        cur = reflect(cur)
    print(len(all_ms))
