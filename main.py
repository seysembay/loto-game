import random
from player import Player
from card import Card
from barrel import Barrel


def main():
    barrel = Barrel()
    player1 = Player(Card(), 1)
    player2 = Player(Card(), 2)

    i = 1
    while True:
        barrel_num = barrel.get_next_val()
        print('----------------------------------------')
        print(f"Новый бочонок: {barrel_num} (осталось {90 - i})")
        i += 1
        player1.show_info()
        if player1.type_player == 'hu':
            winner = player1.check_hu(barrel_num, input("зачеркнуть (y/n): "))
        else:
            winner = player1.check_ai(barrel_num)
        if winner != 'to be':
            print(winner)
            break
        else:
            player2.show_info()
            if player2.type_player == 'hu':
                winner = player2.check_hu(barrel_num, input("зачеркнуть (y/n): "))
            else:
                winner = player2.check_ai(barrel_num)
            if winner != 'to be':
                print(winner)
                break


if __name__ == '__main__':
    main()
