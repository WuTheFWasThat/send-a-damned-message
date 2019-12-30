# import random

# def ordered_cyclic_permute_3(x):
#     n = len(x)
#     seed = sum([ord(l) for l in x])
#     my_rand = random.Random(seed)
#     indices = list(range(n))
#     my_rand.shuffle(indices)
#     chars = [l for l in x]
#     for i in range(0, n-2, 3):
#         ind_1, ind_2, ind_3 = indices[i:i+3]
#         chars[ind_1] = x[ind_2]
#         chars[ind_2] = x[ind_3]
#         chars[ind_3] = x[ind_1]
#     return ''.join(chars)

def ordered_cyclic_permute_3(x):
    n = len(x)
    n3 = (n // 3) * 3
    newchars = [l for l in x]
    for i in range(0, n3 // 3):
        ind_1 = i
        ind_2 = n3 // 3 + i
        ind_3 = 2 * n3 // 3 + i
        if i % 2 == 1:
            ind_2, ind_3 = ind_3, ind_2
        newchars[ind_1] = x[ind_2]
        newchars[ind_2] = x[ind_3]
        newchars[ind_3] = x[ind_1]
    return ''.join(newchars)

