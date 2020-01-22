import os
import readline
from importlib import import_module


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

def register(level):
    levels[level['name']] = level

for file in os.listdir(os.path.join(os.path.dirname(__file__), "levels")):
    if file.endswith(".py"):
        name = file.rstrip(".py")
        try:
            module = import_module(f'levels.{name}', package=f'levels.{name}')
            register(module.level)
        except AttributeError as e:
            raise Exception(f"Failed to import {name}") from e

def smart_input(x, color=None):
    if color is None:
        return input(x)
    y = input(x + _COLORS[color])
    print(_COLORS_END, end='')
    return y


def main(one_player=True, skip=0, dev=False):
    for i, level in enumerate(levels):
        if dev:
            print('=' * 20 + str(i) + ' ' + level['name'] + '=' * 20)
            print(_colored(level['goal'], 'green'))
            print(_colored(level['fn'](level['goal']), 'red'))
        if 'answer' in level:
            if dev:
                print(_colored(level['answer'], 'yellow'))
            assert level['fn'](level['answer']) == level['goal'], f"{level['name']} '{level['fn'](level['answer'])}'"

    def clear_screen():
        if one_player:
            return
        # TODO: better
        for _ in range(1000):
            print()

    def yesno(msg):
        while True:
            w = smart_input(msg)
            if w.lower() in ['y', 'yes']:
                return True
            if w.lower() in ['n', 'no']:
                return False
            print("Unable to parse, please type 'y' or 'n'")

    i = skip
    while True:
        if i >= len(levels):
            print('Congrats!  Game over')
            return
        if i < 0:
            print('Already at level 0')
            i = 0

        level = levels[i]
        print('=' * 40)
        print(f'Level {i}: {level["name"]}')
        print('=' * 40)
        # print(f'Level {i}')
        while True:
            print('-' * 40)
            print('GOAL IS TO SEND:')
            print(_colored(level["goal"], 'green'))
            print()
            x = smart_input('Send your message:\n', color='yellow')
            if x == 'SKIP':
                i += 1
                break
            if x == 'BACK':
                i -= 1
                break
            y = level['fn'](x)
            if y == level['goal']:
                print()
                print(_colored('Passed level!', color='green'))
                clear_screen()
                i += 1
                break
            if not one_player:
                clear_screen()
                smart_input('Pass the laptop! Press enter when laptop has switched hands')
                clear_screen()
                print()
            # yesno('Decode?')
            print('Received damned message:')
            print(_colored(y, 'red'))

if __name__ == "__main__":
    try:
        import fire
        fire.Fire(main)
    except ModuleNotFoundError:
        main()
