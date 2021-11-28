import random

words = ['abruptly\n', 'absurd\n', 'abyss\n', 'affix\n', 'askew\n', 'avenue\n', 'awkward\n', 'axiom\n', 'azure\n',
         'bagpipes\n', 'bandwagon\n', 'banjo\n', 'bayou\n', 'beekeeper\n', 'bikini\n', 'blitz\n', 'blizzard\n',
         'boggle\n', 'bookworm\n', 'boxcar\n', 'boxful\n', 'buckaroo\n', 'buffalo\n', 'buffoon\n', 'buxom\n',
         'buzzard\n', 'buzzing\n', 'buzzwords\n', 'caliph\n', 'cobweb\n', 'cockiness\n', 'croquet\n', 'crypt\n',
         'curacao\n', 'cycle\n', 'daiquiri\n', 'dirndl\n', 'disavow\n', 'dizzying\n', 'duplex\n', 'dwarves\n',
         'embezzle\n', 'equip\n', 'espionage\n', 'euouae\n', 'exodus\n', 'faking\n', 'fishhook\n', 'fixable\n',
         'fjord\n', 'flapjack\n', 'flopping\n', 'fluffiness\n', 'flyby\n', 'foxglove\n', 'frazzled\n', 'frizzled\n',
         'fuchsia\n', 'funny\n', 'gabby\n', 'galaxy\n', 'galvanize\n', 'gazebo\n', 'giaour\n', 'gizmo\n', 'glowworm\n',
         'glyph\n', 'gnarly\n', 'gnostic\n', 'gossip\n', 'grogginess\n', 'haiku\n', 'haphazard\n', 'hyphen\n',
         'iatrogenic\n', 'icebox\n', 'injury\n', 'ivory\n', 'ivy\n', 'jackpot\n', 'jaundice\n', 'jawbreaker\n',
         'jaywalk\n', 'jazziest\n', 'jazzy\n', 'jelly\n', 'jigsaw\n', 'jinx\n', 'jiujitsu\n', 'jockey\n',
         'jogging\n', 'joking\n', 'jovial\n', 'joyful\n', 'juicy\n', 'jukebox\n', 'jumbo\n', 'kayak\n', 'kazoo\n',
         'keyhole\n', 'khaki\n', 'kilobyte\n', 'kiosk\n', 'kitsch\n', 'kiwifruit\n', 'klutz\n', 'knapsack\n',
         'larynx\n', 'lengths\n', 'lucky\n', 'luxury\n', 'lymph\n', 'marquis\n', 'matrix\n', 'megahertz\n',
         'microwave\n', 'mnemonic\n', 'mystify\n', 'naphtha\n', 'nightclub\n', 'nowadays\n', 'numbskull\n', 'nymph\n',
         'onyx\n', 'ovary\n', 'oxidize\n', 'oxygen\n', 'pajama\n', 'peekaboo\n', 'phlegm\n', 'pixel\n', 'pizazz\n',
         'pneumonia\n', 'polka\n', 'pshaw\n', 'psyche\n', 'puppy\n', 'puzzling\n', 'quartz\n', 'queue\n', 'quips\n',
         'quixotic\n', 'quiz\n', 'quizzes\n', 'quorum\n', 'razzmatazz\n', 'rhubarb\n', 'rhythm\n', 'rickshaw\n',
         'schnapps\n', 'scratch\n', 'shiv\n', 'snazzy\n', 'sphinx\n', 'spritz\n', 'squawk\n', 'staff\n',
         'strength\n', 'strengths\n', 'stretch\n', 'stronghold\n', 'stymied\n', 'subway\n', 'swivel\n',
         'syndrome\n', 'thriftless\n', 'thumbscrew\n', 'topaz\n', 'transcript\n', 'transgress\n', 'transplant\n',
         'triphthong\n', 'twelfth\n', 'twelfths\n', 'unknown\n', 'unworthy\n', 'unzip\n', 'uptown\n', 'vaporize\n',
         'vixen\n', 'vodka\n', 'voodoo\n', 'vortex\n', 'voyeurism\n', 'walkway\n', 'waltz\n', 'wave\n', 'wavy\n',
         'waxy\n', 'wellspring\n', 'wheezy\n', 'whiskey\n', 'whizzing\n', 'whomever\n', 'wimpy\n', 'witchcraft\n',
         'wizard\n', 'woozy\n', 'wristwatch\n', 'wyvern\n', 'xylophone\n', 'yachtsman\n', 'yippee\n', 'yoked\n',
         'youthful\n', 'yummy\n', 'zephyr\n', 'zigzag\n', 'zigzagging\n', 'zilch\n', 'zipper\n', 'zodiac\n', 'zombie']

writeon = open("words.xd", "a")

for i in words:
    i = i.lower()
    i = i.strip()
    writeon.writelines(i + '\n')

writeon.close()