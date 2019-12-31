from utils import rotate_alphabet, alphabet

"""
TODO: a terrible programmer wrote this whole file, there are probably bugs
"""
def _switchbacks_reduce_path(path):
    if not len(path):
        return []
    segments = []
    cur_dir = None
    last = None
    segment = []
    for char in path:
        if last is not None:
            new_dir = ord(char.lower()) - ord(last.lower())
            if abs(new_dir) > 1:
                segments.append((segment + [last], cur_dir or 0))
                sign = 1 if new_dir > 0 else -1
                segments.append(([
                    rotate_alphabet(last, sign),
                    rotate_alphabet(char, -sign)
                ], 'Jump'))
                segment = []
                cur_dir = None
            elif cur_dir is None:
                segment.append(last)
                cur_dir = new_dir
            elif new_dir != cur_dir:
                if cur_dir == 0 and new_dir != 0:
                    segment.append(last)
                segments.append((segment, cur_dir))
                segment = []
                if new_dir == 0:
                    segment.append(last)
                elif cur_dir != 0:  # V or ^ shape
                    segments.append(([last], 0))
                cur_dir = new_dir
            else:
                segment.append(last)
        last = char
    assert last is not None
    segments.append((segment + [last], cur_dir or 0))

    result = []
    print('segments', segments)
    for i, (segment, dir) in enumerate(segments):
        assert dir in [-1, 1, 0, 'Jump']
        if dir == 0:
            if i > 0 and i < len(segments) - 1 and segments[i-1][1] == segments[i+1][1] and segments[i-1][1] != 'Jump':
                segment = segment[1:]
        if dir in [-1, 1]:
            # print('i', i, segments)
            if i > 0 and segments[i-1][1] == 'Jump':
                pass
            elif i < len(segments) - 1 and segments[i+1][1] == 'Jump':
                pass
            else:
                if i == 0:
                    result.append(segment[0])
                if i == len(segments) - 1:
                    result.append(segment[-1])
                segment = []
        result.extend(segment)
        # print('segment', segment, 'new result', result)

    # print('result', result)
    return result

def test_switchbacks(s, expected):
    actual = ''.join(_switchbacks_reduce_path(list(s)))
    assert actual == expected, f'{actual} != {expected}'

test_switchbacks('', '')
test_switchbacks('m', 'm')
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
