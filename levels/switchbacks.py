from utils import rotate_alphabet, alphabet

"""
TODO: a terrible programmer wrote this whole file, there are probably bugs
"""
def _switchbacks_reduce_path(path):
    if not len(path):
        return []
    segments = []
    # NOTE: none means undetermined, not jump (confusing since it means jump in the segments array
    cur_dir = None
    segment = []
    for char in path:
        if len(segment):
            new_dir = ord(char.lower()) - ord(segment[-1].lower())
            if abs(new_dir) > 1:
                segments.append((segment, cur_dir or 0))
                sign = 1 if new_dir > 0 else -1
                segments.append(([
                    rotate_alphabet(segment[-1], sign),
                    rotate_alphabet(char, -sign)
                ], None))
                segment = []
                cur_dir = None
            elif cur_dir is None:
                cur_dir = new_dir
            elif new_dir != cur_dir:
                segments.append((segment, cur_dir or 0))
                segment = []
                if new_dir == 0:
                    last = segments[-1][0].pop()
                    segment.append(last)
                elif segments[-1][1] != 0:
                    last = segments[-1][0].pop()
                    segments.append(([last], 0))
                cur_dir = new_dir
        segment.append(char)
    segments.append((segment, cur_dir or 0))

    result = []
    # print('segments', segments, growleft, growright)
    for i, (segment, dir) in enumerate(segments):
        if dir is None:
            result.extend(segment)
        elif dir == 0:
            if i > 0 and i < len(segments) - 1 and segments[i-1][1] == segments[i+1][1] and segments[i-1][1] != None:
                result.extend(segment[1:])
            else:
                result.extend(segment)
        elif dir != 0:
            # print('i', i, segments)
            if i > 0 and segments[i-1][1] == None:
                result.extend(segment)
            elif i < len(segments) - 1 and segments[i+1][1] == None:
                result.extend(segment)
            else:
                if i == 0:
                    result.append(segment[0])
                if i == len(segments) - 1:
                    result.append(segment[-1])
        # print('segment', segment, 'new result', result)

    # print('result', result)
    return result

def test_switchbacks(s, expected):
    actual = ''.join(_switchbacks_reduce_path(list(s)))
    assert actual == expected, f'{actual} != {expected}'

test_switchbacks('jklmz', 'jklmnyz')
test_switchbacks('ajklm', 'abijklm')
test_switchbacks('jklm', 'jm')
test_switchbacks('abjklmyz', 'abcijklmnxyz')
test_switchbacks('abjjyz', 'abcijjkxyz')

test_switchbacks('aabcdef', 'aaf')
test_switchbacks('aabcdeft', 'aabcdefgst')
test_switchbacks('taabcdef', 'tsbaaf')

test_switchbacks('tabcdeff', 'tsbabcdeff')
test_switchbacks('abcdeff', 'aff')
test_switchbacks('abcdefft', 'affgst')

test_switchbacks('abcba', 'aca')
test_switchbacks('abababa', 'abababa')

test_switchbacks('abbc', 'abc')
test_switchbacks('abcdeffedcbabccd', 'affacd')
test_switchbacks('tabcdeffedcbabccd', 'tsbabcdeffacd')

def switchbacks(x):
    """
    Paths reach for each other, also break if there are two switches
    """

    result = []
    curpath = []
    for char in x:
        if char.lower() not in alphabet:
            result.extend(_switchbacks_reduce_path(curpath))
            curpath = []
            result.append(char)
        else:
            curpath.append(char)
    result.extend(_switchbacks_reduce_path(curpath))
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
