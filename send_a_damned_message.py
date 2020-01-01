import fire
import readline

from levels.rot_word import level as rot_word
from levels.substitution import level as substitution
from levels.cancer import level as cancerous_vowels
from levels.quote import level as quote_hell
from levels.step import level as extend_sequences
from levels.paths import level as paths
from levels.unary import level as count_words
from levels.palindrome import level as needs_palindromic_redundancy
from levels.cycle3 import level as ordered_cyclic_permute_3
from levels.lonely import level as lonely_death
from levels.corrupt import level as corrupt
from levels.codebook import level as codebook
from levels.explode import level as explode
from levels.reflect import level as reflect
from levels.checksum import level as checksum
from levels.sandwiched import level as cut_sandwiched
from levels.end import level as end

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

- delete in between all double letters?
  - some ordering to make it possible?
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
    # dict(
    #     name='One',
    #     fn=count_words_unimplemented,
    #     goal='1 damned message',
    #     answer='a1a 1d1a1m1n1e1d1 1m1e1s1s1a1g1e',
    # ),

    rot_word,
    # substitution, # meh level
    extend_sequences,
    count_words,
    # checksum, # meh level
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
        name='Cut',
        fn=cut_sandwiched,
        goal='a damned message',
        answer='axx damneyyd meszzsage',
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
        name='Darn',  # 'Corrupt',
        fn=corrupt,
        goal='a damned message b',
        answer='a damned messagp b',
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
        name='Quote',  # TODO: make this level better / less confusing?
        fn=quote_hell,
        goal='"Send a damned message", I demanded',
        answer='", I demanded"""Send a damned message""'
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
