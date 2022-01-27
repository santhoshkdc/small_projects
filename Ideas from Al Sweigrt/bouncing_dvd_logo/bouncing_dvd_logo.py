import sys, random, time

try:
    import bext
except ImportError:
    print("""bext module is not available on this device""")

WIDTH, HEIGHT = bext.size()
w, h = WIDTH, HEIGHT
COLOR = 'color'
X = "x"
Y = 'y'
DIR = 'direction'
NUMBER_OF_LOGOS = 5
PHASE_TIME = 0.02
colors = ['red', 'blue', 'green', 'yellow', 'white', 'cyan']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
directions = [ UP_RIGHT, UP_LEFT , DOWN_RIGHT, DOWN_LEFT]


def main():
    bext.clear()
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logo = {COLOR : random.choice(colors),
                X : random.randint(0, w-3),
                Y: random.randint(0, h-3),
                DIR: random.choice(directions)}
        if logo[X] % 2 == 1:
            logo[X] -= 1
        logos.append(logo)

    corner_bounce = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')


            originaldirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                corner_bounce += 1
            elif logo[X] == 0 and logo[Y] == h - 1:
                corner_bounce += 1
            elif logo[X] == w - 3 and logo[Y] == h - 1:
                corner_bounce += 1
            elif logo[X] == w - 3 and logo[Y] == 0:
                corner_bounce += 1

            #left edge
            if logo[DIR] == UP_LEFT and logo[X] == 0:
                logo[DIR] = UP_RIGHT
            elif logo[DIR] == DOWN_LEFT and logo[X] == 0:
                logo[DIR] = DOWN_RIGHT

            #right edge
            if logo[DIR] == DOWN_RIGHT and logo[X] == w - 3:
                logo[DIR] = DOWN_LEFT
            elif logo[DIR] == UP_RIGHT and logo[X] == w - 3:
                logo[DIR] = UP_LEFT

            # top edge
            if logo[DIR] == UP_RIGHT and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
            elif logo[DIR] == UP_LEFT and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT

            # bottom edge
            if logo[DIR] == DOWN_RIGHT and logo[Y] == h - 1:
                logo[DIR] = UP_RIGHT
            elif logo[DIR] == DOWN_LEFT and logo[Y] == h - 1:
                logo[DIR] = UP_LEFT

            if logo[DIR] != originaldirection:
                logo[COLOR] = random.choice(colors)

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5,0)
        bext.fg('white')
        print("Corner Bounces:", corner_bounce, end='')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end='')

        time.sleep(PHASE_TIME)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()