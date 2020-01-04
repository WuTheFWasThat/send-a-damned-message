def ordered_cyclic_permute_3(x):
    k = 3
    n = len(x)
    nk = (n // k)
    newchars = [l for l in x]
    for i in range(0, nk):
        inds = [i + nk * j for j in range(k)]
        for j in range(3):
            # natural version but with some stationary chars
            # newchars[inds[j]] = x[inds[(j + i) % k]]
            newchars[inds[j]] = x[inds[(j + (1 if i % 2 == 0 else -1)) % k]]
    return ''.join(newchars)
