from player import Player
from card import Card
from barrel import Barrel
from constants import TOBE, HU


def main():
    barrel = Barrel()
    player_count = int(input("Введите количество игроков: "))
    players = []
    for player_num in range(player_count):
        players.append(Player(Card(), player_num+1))
    i = 1
    while True:
        barrel_num = barrel.get_next_val()
        print('----------------------------------------')
        print(f"Новый бочонок: {barrel_num} (осталось {90 - i})")
        end = False
        i += 1
        for player in players:
            player.show_info()
            if player.type_player == HU:
                winner = player.check_hu(barrel_num, input("зачеркнуть (y/n): "))
            else:
                winner = player.check_ai(barrel_num)
            if winner != TOBE:
                print(winner)
                end = True
                break
        if end:
            break


if __name__ == '__main__':
    main()
