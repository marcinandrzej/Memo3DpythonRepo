from GameClass import GameClass

WINDOW_W = 800
WINDOW_H = 600


def main():

    game = GameClass(WINDOW_W, WINDOW_H)

    while True:
        game.eventLoopProcessing()

        game.checkWinCondition()

        game.drawGame()


if __name__ == '__main__': main()

