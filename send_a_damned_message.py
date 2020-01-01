import fire
import readline

from levels.rot_word import rot_word
from levels.substitution import substitution
from levels.cancer import cancerous_vowels
from levels.quote import quote_hell
from levels.step import extend_sequences
from levels.paths import paths
from levels.unary import count_words
from levels.palindrome import needs_palindromic_redundancy
from levels.cycle3 import ordered_cyclic_permute_3
from levels.lonely import lonely_death
from levels.corrupt import corrupt
from levels.codebook import codebook
from levels.explode import explode
from levels.reflect import reflect
from levels.checksum import checksum

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
- Maybe something based on factorization?
- accumulate sum within word?
- solving equations?
"""
levels = [
    dict(
        name='Id',
        fn=lambda x: x,
        goal='a damned message',
        answer='a damned message',
    ),
    dict(
        name='Cut',
        fn=lambda x: x[:-len(x.split(' '))],
        goal='a damned message',
        answer='a damned message...',
    ),
    dict(
        name='Rot',
        fn=rot_word,
        goal='a damned message',
        answer='amnedd essagem a',
    ),
    # dict(
    #     name='Sub',
    #     fn=substitution,
    #     goal='a damned message',
    #     answer='t ztyjez yevvtxe',
    # ),
    dict(
        name='Ext',  # extend, extrapolate
        fn=extend_sequences,
        goal='a damned message',
        answer="a daklngfd meqrutage"
    ),
    dict(
        name='Un',
        fn=count_words,
        goal='Damn it',
        answer='DDDDammmmmmmmmmmmmnnnnnnnnnnnnnn iiiiiiiiitttttttttttttttttttt',
    ),
    # dict(
    #     name='Check',
    #     fn=checksum,
    #     goal='a damned message',
    #     answer='aa damnedo messageq',
    # ),
    dict(
        name='Corrupt',  # TODO: make this level better
        fn=corrupt,
        goal='damn',
        # answer='a damned message',
        # answer='z damned messagea',
        # answer='a damned message ',
    ),
    dict(
        name='Crypt',  # 'Why',  # Lonely?
        fn=lonely_death,
        goal='a damned message',
        answer='ay dyamneyd myessaygey',
    ),
    dict(
        name='Lap',  # fold?
        fn=needs_palindromic_redundancy,
        goal='a damned message',
        answer='a damned messageegassem denmad a',
    ),
    dict(
        name='Cancer',
        fn=cancerous_vowels,
        goal='a damned message',
        answer='a  d a mn e d m e ss a g e ',
    ),
    dict(
        name='Reflect',
        fn=reflect,
        goal='a damned message',
        answer='egs dma danemesa',
    ),
    dict(
        name='Book',
        fn=codebook,
        goal='a damned message',
        answer='adamnedmessage a bcdefg hijklmn',
    ),
    dict(
        name='Group',  # 'Trippy',
        fn=explode,
        goal='please, just a short damned message',
        # answer=' ( please, ( just a)) ( short ( damned message))',
        answer=' ( please, ( just ( a ( short ( damned message'
    ),
    dict(
        name='Tricky',
        fn=ordered_cyclic_permute_3,
        goal='a really really really really really really really really really stupidly damned long message',
        answer='aylet liaryylae elalryglee laare  laurydle  lmardyloe  lasrygllarsylpe lladrynle  lnarmylse e',
    ),
    dict(
        name='Hike',  # W
        fn=paths,
        goal='a damned message',
        answer='a dcbabcdefghijklmmnmlkjihgfeed mlkjihgfefghijklmnopqrssrqponmlkjihgfedcbabcdefgfe',
        # answer="Send a daklpocdbc meqrutage"
    ),
    dict(
        name='Quote',  # TODO: make this level better
        fn=quote_hell,
        goal='"Send a damned message", I said',
        answer='", I said"""Send a damned message""'
    ),
    # dict(
    #     name='Quote',
    #     fn=quote_hell_old,
    #     goal='"She said, \'Send a damned message\'", he said',
    #     answer="""
    #     '"She said, '"message' damned a 'Send"'", he said'
    #     """.strip(),
    #     # answer="""
    #     # '", he said'"'"'Send a damned message'"'"'"She said, '
    #     # """.strip(),
    # ),
]

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
            print(_colored(level['answer'], 'yellow'))

        if 'answer' in level:
            assert level['fn'](level['answer']) == level['goal'], f"'{level['fn'](level['answer'])}'"

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
                smart_input('Passed level!  Enter to continue')
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
            print()

if __name__ == "__main__":
    fire.Fire(main)
