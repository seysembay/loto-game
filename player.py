import random


class Player:
    def __init__(self, card):
        types = ["ai", "hu"]
        player_names = ['Tor', 'Cap', 'Vanda', 'Hulk', 'Suren']
        player1_type = input("Выберите тип игрока N1 (ai/hu): ")
        if player1_type not in types:
            print("Некорректный тип игрока!")
            return
        elif player1_type == "ai":
            player1_name = random.choice(player_names)
        else:
            player1_name = input("Введите имя игрока N1: ")
        self.name = player1_name
        self.type_player = player1_type
        self.card = card

    def __str__(self):
        return f'{self.name} {self.type_player}'
