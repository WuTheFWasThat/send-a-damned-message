import readline

from levels.substitution import substitution
from levels.paths import paths
from levels.corrupt import corrupt_final as corrupt
from levels.explode import explode
from levels.please import please
from levels.reflect import reflect
from levels.checksum import checksum
from levels.sandwiched import reverse_sandwiched
from levels.tournament import tournament
from levels.ctrl import ctrl
from levels.madden import fn as madden

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
levels = [
    # dict(
    #     name='Ctrl',
    #     fn=ctrl,
    #     goal='a damned message',
    #     answer='ec gc ac scc ec mc db eb nb mb ab db aa',
    # ),
    dict(
        name='Madden',
        fn=madden,
        goal='a damned message demands a sage me',
        answer='sem denmad aassdnamed eggas a  eem',
        # goal='a damned message a sage me demands',
        # answer='sem denmad aassdnamed em egas a eg'
        # answer='ssem denmad a dneegas',
        # goal='need dam massage',
        # answer='',
        # answer='a damned message',
    ),
    # dict(
    #     name='Sub',
    #     fn=substitution,
    #     goal='a damned message',
    #     answer='t ztyjez yevvtxe',
    # ),
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
        name='Milk',  # Reflect
        fn=reflect,
        goal="a damned message",
        answer="easmdna adme esg",
    ),
    # dict(
    #     name='Book (Alt)',
    #     fn=book_unimplemented,
    #     goal='a damned message',
    #     answer='a a b damned c message abc',
    # ),
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
        name='Darn',  # 'Corrupt',
        fn=corrupt,
        goal='a damned message',
        answer='a damned messagp',
        # goal='a damned b message',
        # answer='a damned b messlge',
        # goal='a damned messaaage',
        # answer='a damned messaalge',
        # goal='a darn massage',
        # answer='a darn bassage',
        # goal='a damnn msg plz',
        # answer='l damnn msg plz',
    ),
    dict(
        name='Please',  # 'Trippy',
        fn=please,
        goal='a (short) damned message, pretty pretty please!!',
        answer='a (!(short!) (damned (message, (pretty (pretty (please!!!!',
        # answer=""" ( please, ( just ( a ( short ( damned message"""
    ),
    # dict(
    #     name='Group',  # 'Trippy',
    #     fn=explode,
    #     goal='(please) send a short "damned" message wouldn\'t you?',
    #     answer='() \'(please) send a short "damned" message\' "wouldn\'t you?"',
    #     # answer=""" ( please, ( just ( a ( short ( damned message"""
    # ),
    dict(
        name='Cut',
        fn=reverse_sandwiched,
        goal='a damned message',
        answer='ad aged mnemasse',
    ),
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
