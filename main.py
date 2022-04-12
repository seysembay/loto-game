import random
from player import Player
from card import Card


def main():

    player1_card = Card()
    player1 = Player(player1_card)
    print(player1)
    player1_card.show_card()

    player2_card = Card()
    player2 = Player(player2_card)
    print(player2)
    player2_card.show_card()


if __name__ == '__main__':
    main()
