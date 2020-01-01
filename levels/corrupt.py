from utils import alphabet


def num(l):
    if l.lower() not in alphabet:
        return 0
    return (ord(l.lower()) - ord('a') + 1) % 26


def corrupt(x):
    """
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    """
    if not len(x):
        return x
    total = sum([num(l) for l in x])
    index = (total - 1) % len(x)
    new_num = (num(x[index]) + total - 1) % 26
    new = chr(new_num + ord('a'))
    return x[:index] + new + x[index + 1:]

# NOTE: sum(dar) = sum(ned)
# 4 1 18 14 5 4

# NOTE: sum(damn)
# 4 1 13 14

for offset in range(7):
    for addlength in range(5):
        total_length = offset + 4 + addlength
        for total_sum in range(offset+3, total_length * 20, total_length):
            remaining_sum = total_sum - sum([num(l) for l in 'damn'])
            if remaining_sum < 0:
                continue
            if not total_sum % 26 == 5:
                continue
            # now make sure a corruption exists
            for corrupt_amt in range(-26, 26):
                corrupted_sum = total_sum + corrupt_amt
                for index in range(total_length):
                    if (corrupted_sum - 1) % total_length != index:
                        continue
                    # print('corrupted sum', corrupted_sum % 26, (corrupt_amt) % 26)
                    if corrupted_sum % 26 != (-corrupt_amt) % 26:
                        continue
                    print('works', offset, addlength, 'remain sum', remaining_sum, 'corrupt', corrupt_amt, 'index')

print('DAMN', corrupt('damnml'))
# goal = 'this damned message'
# print('DAMN', corrupt(goal))
# s = set()
# for i in range(len(goal)):
#     for x in alphabet + ' ':
#         test = goal[:i] + x + goal[i+1:]
#         # print(test, corrupt(test))
#         # if corrupt(test) in s:
#         #     print('repeat', corrupt(test))
#         s.add(corrupt(test))
#         if corrupt(test) == goal:
#             print(test, corrupt(test))
#             # raise Exception(test)
# print(sum([num(l) for l in 'damn']))
