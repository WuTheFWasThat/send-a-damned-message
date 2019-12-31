from utils import rotate_alphabet, alphabet

"""
TODO: a terrible programmer wrote this whole file, there are probably bugs
"""
def _switchbacks_reduce_path(path, growleft, growright):
    segments = []
    cur_dir = 0
    segment = [path[0]]
    for char in path[1:]:
        new_dir = ord(char.lower()) - ord(segment[-1].lower())
        assert abs(new_dir) <= 1
        if new_dir != cur_dir:
            segments.append((segment, cur_dir))
            if cur_dir != 0:
                last = segment.pop()
                if new_dir != 0:
                    segments.append(([last], 0))
            segment = []
            if new_dir == 0:
                segment.append(last)
        segment.append(char)
        cur_dir = new_dir
    segments.append((segment, cur_dir))
    if cur_dir != 0:
        last = segment.pop()
        segments.append(([last], 0))

    result = []
    # print('segments', segments, growleft, growright)
    for i, (segment, dir) in enumerate(segments):
        if i % 2 == 0:
            assert dir == 0
            if i > 1 and i < len(segments) - 2 and segments[i-1][1] == segments[i+1][1]:
                result.extend(segment[1:])
            else:
                result.extend(segment)
        else:
            assert dir != 0
            if i == 1 and len(segments[0][0]) == 1 and growleft:
                result.extend(segment)
            elif i == len(segments) - 2 and len(segments[-1][0]) == 1 and growright:
                result.extend(segment)
        # print('segment', segment, 'new result', result)

    # print('result', result)
    return result

def test_switchbacks(s, growleft, growright, expected):
    actual = ''.join(_switchbacks_reduce_path(list(s), growleft, growright))
    assert actual == expected, f'{actual} != {expected}'

test_switchbacks('abcdef', True, False, 'abcdef')
test_switchbacks('abcdef', False, True, 'abcdef')
test_switchbacks('abcdef', False, False, 'af')

test_switchbacks('aabcdef', True, False, 'aaf')
test_switchbacks('aabcdef', False, True, 'aabcdef')
test_switchbacks('aabcdef', False, False, 'aaf')

test_switchbacks('abcdeff', True, False, 'abcdeff')
test_switchbacks('abcdeff', False, True, 'aff')
test_switchbacks('abcdeff', False, False, 'aff')

test_switchbacks('abababa', False, False, 'abababa')

test_switchbacks('abcdeffedcbabccd', True, False, 'abcdeffacd')

def switchbacks(x):
    """
    Paths reach for each other, also break if there are two switches
    """

    result = []
    curpath = []
    growleft = False
    for char in x:
        if char.lower() not in alphabet:
            if len(curpath):
                result.extend(_switchbacks_reduce_path(
                    curpath, growleft=growleft, growright=False
                ))
            curpath = []
            growleft = False
            result.append(char)
        else:
            if len(curpath):
                diff = ord(char.lower()) - ord(curpath[-1].lower())
                if abs(diff) > 1:
                    sign = 1 if diff > 0 else -1
                    result.extend(_switchbacks_reduce_path(
                        curpath, growleft=growleft, growright=True
                    ))
                    result.append(rotate_alphabet(curpath[-1], sign))
                    result.append(rotate_alphabet(char, -sign))
                    curpath = []
                    growleft = True
            curpath.append(char)
    if len(curpath):
        result.extend(_switchbacks_reduce_path(
            curpath, growleft=growleft, growright=False
        ))
    return ''.join(result)

"""
if 1:
    all_ms = set()
    cur = 'a damned message'
    while True:
        print(cur)
        if cur in all_ms:
            break
        all_ms.add(cur)
        cur = switchbacks(cur)
"""
