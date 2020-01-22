import os
import readline
from importlib import import_module
import sys

_COLORS = dict(
    green="\033[92m",
    blue="\033[94m",
    red="\033[91m",
    yellow="\033[93m",
)
_COLORS_END = "\033[0m"
def _colored(t, color):
    return _COLORS[color] + t + _COLORS_END

"""
- accumulate sum within word?

- massage?
- madman, madam

- something tree-like
- something using fact that 'a damned message' length is power of two
"""
# dict(
#     name='One',
#     fn=count_words_unimplemented,
#     goal='1 damned message',
#     answer='a1a 1d1a1m1n1e1d1 1m1e1s1s1a1g1e',
# ),
# dict(
#     name='Book (Alt)',
#     fn=book_unimplemented,
#     goal='a damned message',
#     answer='a a b damned c message abc',
# ),

levels = dict()
for file in os.listdir(os.path.join(os.path.dirname(__file__), "levels")):
    if file.endswith(".py"):
        name = file.rstrip(".py")
        try:
            module = import_module(f'levels.{name}', package=f'levels.{name}')
            levels[name] = module.level
        except AttributeError as e:
            raise Exception(f"Failed to import {name}") from e


def smart_input(x, color=None):
    if color is None:
        return input(x)
    y = input(x + _COLORS[color])
    print(_COLORS_END, end='')
    return y


def main(level_name):
    if level_name not in levels:
        print('Available levels: ')
        print('\n'.join(levels.keys()))
        return
    level = levels[level_name]
    if 'answer' in level:
        print(_colored(level['answer'], 'yellow'))
        assert level['fn'](level['answer']) == level['goal'], f"{level['fn'](level['answer'])}"

    print('=' * 40)
    print(f'Level {level_name}')
    print('=' * 40)
    # print(f'Level {i}')
    while True:
        print('-' * 40)
        print('GOAL IS TO SEND:')
        print(_colored(level["goal"], 'green'))
        print()
        x = smart_input('Send your message:\n', color='yellow')
        y = level['fn'](x)
        if y == level['goal']:
            print()
            print(_colored('Passed level!', color='green'))
            break
        print('Received damned message:')
        print(_colored(y, 'red'))

if __name__ == "__main__":
    main(sys.argv[1])
