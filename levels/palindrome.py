def needs_palindromic_redundancy(x):
    recovered = []
    letters = list(x)
    while len(letters) > 1:
        start = letters.pop(0)
        end = letters.pop(-1)
        if start == end:
            recovered.append(start)
        else:
            break
    return ''.join(recovered)
