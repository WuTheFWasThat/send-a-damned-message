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
from levels.sandwiched import reverse_sandwiched
from levels.end import end
from levels.tournament import tournament
from levels.caps import caps
from levels.chain_define import chain_define

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

- something tree-like
- something using fact that 'a damned message' length is power of two
"""
levels = [
    dict(
        name='Id',
        fn=lambda x: x,
        goal='a damned message',
        answer='a damned message',
    ),
    dict(
        name='Trim',
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
    dict(
        name='Caps',  # 'Case', 'Upper'
        fn=caps,
        goal='A DAMNED MESSAGE',
        answer='A dAmnEd MesSagE',
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
    #     name='One',
    #     fn=count_words_unimplemented,
    #     goal='1 damned message',
    #     answer='a1a 1d1a1m1n1e1d1 1m1e1s1s1a1g1e',
    # ),
    # dict(
    #     name='Check',
    #     fn=checksum,
    #     goal='a damned message',
    #     answer='aa damnedo messageq',
    # ),
    dict(
        name='Mum',  # Lap',  # fold?
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
        name='Milk',  # Reflect
        fn=reflect,
        goal='yet another damned message',
        answer='easmdna etn eytaohrdme esg',
    ),
    dict(
        name='Book',
        fn=codebook,
        goal='a damned message',
        # answer='adamnedmessage a bcdefg hijklmn',
        answer='abcdefghijklmnopqrs a damned message',
    ),
    # dict(
    #     name='Book',
    #     fn=book_unimplemented,
    #     goal='a damned message',
    #     answer='a a b damned c message abc',
    # ),
    dict(
        name='Crypt',  # 'Why',  # Lonely?
        fn=lonely_death,
        goal='a damned message',
        answer='ay dyamneyd myessaygey',
    ),
    dict(
        name='Hike',  # W
        fn=paths,
        goal='a damned message',
        answer='a dcbabcdefghijklmmnmlkjihgfeed mlkjihgfefghijklmnopqrssrqponmlkjihgfedcbabcdefgfe',
        # answer="Send a daklpocdbc meqrutage"
    ),
    # dict(
    #     name='Tree',
    #     fn=tournament,
    #     goal='a damned message',
    #     answer='k caunadqmmskabe',
    # ),
    dict(
        name='Def',
        fn=chain_define,
        goal='a damned b message abc',
        answer='x  d y  b z  m w  a axamnedyzessagewbc',
    ),
    dict(
        name='Darn',  # 'Corrupt',
        fn=corrupt,
        goal='a damned b message',
        answer='a damned b messlge',
        # goal='a damned messaaage',
        # answer='a damned messaalge',
        # goal='a darn massage',
        # answer='a darn bassage',
        # goal='a damnn msg plz',
        # answer='l damnn msg plz',
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
        goal=(
            'a damned message which contains as many usages of "damned" as possible, was damned by the damned over and over, and was deliberately constructed to be unnecessarily damned long (and confusing)'
        ),
        answer=ordered_cyclic_permute_3(ordered_cyclic_permute_3(
            'a damned message which contains as many usages of "damned" as possible, was damned by the damned over and over, and was deliberately constructed to be unnecessarily damned long (and confusing)'
        )),
    ),
    # dict(
    #     name='Quote',  # TODO: make this level better / less confusing?
    #     fn=quote_hell,
    #     goal='I received a demand to "Send a damned message"',
    #     answer='", I demanded"""Send a damned message""'
    # ),
    dict(
        name='Cut',
        fn=reverse_sandwiched,
        goal='a damned message',
        answer='ad aged mnemasse',
    ),
    dict(
        name='End',
        fn=end,
        goal='end all the damned messages',
        answer='send all the damned messages',
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
