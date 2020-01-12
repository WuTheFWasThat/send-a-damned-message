from utils import alphabet, a2num, rotate_alphabet


def corrupt(x, extra_index=0, extra_rotate=0):
    """
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    Everything is mod 27 instead of 26 to make things work out better
    """
    if not len(x):
        return x
    total = sum([a2num(l, with_spaces=True) for l in x])
    index = (total - 1 + extra_index) % len(x)
    new = rotate_alphabet(x[index], total + extra_rotate, with_spaces=True)
    return x[:index] + new + x[index + 1:]

"""
16th thing is 6
i=10
for seq in $(grep ' ,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,6,' $oeis_file | cut -d ' ' -f 1 | tail -n +$i); do
    curl -s "https://oeis.org/search?q=$seq&fmt=json" | jq -r '.results[0] | [.number, .name, .data, .comment, .program]';
    read;
    i=$((i+1))
done
"""
# print(corrupt('a damned massage', extra_index=10, extra_rotate=6))
# print(corrupt('a damned message', extra_index=6, extra_rotate=2))
# print(corrupt('a damned messagp', extra_index=6, extra_rotate=2))
# print(corrupt('n'))
# print(corrupt('damged'))
# print(corrupt('message'))


def corrupt_final(x):
    """
    Corruption by adding amount to a single position of each word
    Amount/position both determined by sum of letters
    Everything is mod 27 instead of 26 to make things work out better
    """
    n = len(x)
    if not n:
        return x
    total = sum([a2num(l, with_spaces=True) for l in x])
    index = (total + (n // 3)) % len(x)
    new = rotate_alphabet(x[index], total + (n // 8), with_spaces=True)
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
                remaining_sum = total_sum - sum([a2num(l, with_spaces=True) for l in startword])
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
    goal = 'a damned message'
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


### SECTION TRYING TO MAKE IT WORK WITH EACH WORD
### NOTE: slightly unnatural due to lack of spaces in combination with mod 27
### VERDICT: meh

if 0:
    print(corrupt('a', extra_index=0, extra_rotate=0))
    print(corrupt('damned', extra_index=4, extra_rotate=18))
    print(corrupt('message', extra_index=3, extra_rotate=8))

    """
    0 ? ? ? ? 4 3
    0 ? ? ? ? 18 8

    oeis_file=~/Downloads/stripped
    # for seq in $(grep ' ,0,.,.,.,.,4,3,' $oeis_file | cut -d ' ' -f 1 ); do
    for seq in $(grep ' ,0,.,.,.,.,18,8,' $oeis_file | cut -d ' ' -f 1 ); do
        open "https://oeis.org/search?q=$seq";
        read;
    done
    for seq in $(grep ' ,0,.,.,.,.,18,35,' $oeis_file | cut -d ' ' -f 1 ); do
        open "https://oeis.org/search?q=$seq";
        read;
    done
    """
    # extra index patterns ():
    # A002308 Consecutive quadratic nonresidues mod p
    # Decimal expansion of 1/109, 1/206, 1/223, 1/287, 1/570, 1/656
    # A024222 Number of shuffles (perfect faro shuffles with cut) required to return a deck of size n to original order.
    # A029578 natural numbers interleaved with the even numbers
    # A030451 a(2*n) = n, a(2*n+1) = n+2.
    # A050493 sum of binary digits of n-th triangular number.
    # A050514 (52 % n)
    # A055119 Base-9 complement of n (write n in base 9, then replace each digit with its base-9 negative).
    #         0, 8, 7, 6, 5, 4, 3, 2, 1, 72, 80, 79,
    # a056969 10^n % n
    # a068527 Difference between smallest square >= n and n. (math.ceil(math.sqrt(n))**2 - n)

