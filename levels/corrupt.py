from utils import alphabet


def num(l):
    if l.lower() not in alphabet:
        return 0
    return (ord(l.lower()) - ord('a') + 1) % 27


def corrupt(x):
    """
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    Everything is mod 27 instead of 26 to make things work out better
    """
    if not len(x):
        return x
    total = sum([num(l) for l in x])
    index = (total - 1) % len(x)
    new_num = (num(x[index]) + total) % 27
    if new_num == 0:
        new = ' '
    else:
        new = chr(new_num - 1 + ord('a'))
    return x[:index] + new + x[index + 1:]

if 0:
    startword = 'darn'
    wantdiff = 22
    startword = 'damn'
    wantdiff = 5
    indexdiff = 3

    # search for good sums
    for offset in range(7):
        for addlength in range(14):
            total_length = offset + len(startword) + addlength
            for total_sum in range(offset + indexdiff, total_length * 22, total_length):
                remaining_sum = total_sum - sum([num(l) for l in startword])
                if remaining_sum <= 0:
                    continue
                if not total_sum % 27 == wantdiff:
                    continue
                # now make sure a corruption exists
                for corrupt_amt in range(1, 26):
                    corrupted_sum = total_sum + corrupt_amt
                    for index in range(total_length):
                        if (corrupted_sum - 1) % total_length != index:
                            continue
                        # print('corrupted sum', corrupted_sum % 27, (corrupt_amt) % 26)
                        if corrupted_sum % 27 != (-corrupt_amt) % 27:
                            continue
                        print('works', offset, addlength, 'remain sum', remaining_sum, 'corrupt', corrupt_amt, 'index')

# NOTE: sum(dar) = sum(ned)
# 4 1 18 14 5 4

# NOTE: sum(damn)
# 4 1 13 14

# it = 9 + 20 = 29
# you = 25 + 15 + 21 = 61
# god = 7 + 15 + 4 = 26
# gosh = 7 + 15 + 20 + 8 = 26
# msg = 13 + 19 + 7 = 39

# print(corrupt('god a damn'))
# print(corrupt('a  goddamn'))
# print(corrupt('damn yaa'))
# print(corrupt('damn FU'))
# print(corrupt('damn aok'))
# print(corrupt('a damn mssgv'))
# print(corrupt('a damnn msg plz'))
# print(corrupt('a damned mssg plzm'))
# print(corrupt('a damned messaaage'))
# print(corrupt('a damned message b'))
# print(corrupt('daaaaaamn yoou!'))
# print(corrupt('a darn messaga'))

if 0:
    goal = 'this damned message'
    goal = 'a damnn msg plz'
    goal = 'a damned messaaage'
    goal = 'a darn massage'
    print('DAMN', corrupt(goal))
    s = set()
    for i in range(len(goal)):
        for x in alphabet + ' ':
            test = goal[:i] + x + goal[i + 1:]
            # print(test, corrupt(test))
            # if corrupt(test) in s:
            #     print('repeat', corrupt(test))
            s.add(corrupt(test))
            if corrupt(test) == goal:
                print(test, corrupt(test))
                # raise Exception(test)
    print(sum([num(l) for l in 'damn']))
