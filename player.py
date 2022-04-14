import random
from card import Card
from barrel import Barrel


class Player:
    def __init__(self, card: Card, number: int):
        self.number = number
        self.count_checked_items = 0
        types = ["ai", "hu"]
        player_names = ['Tor', 'Cap', 'Vanda', 'Hulk', 'Suren']
        player_type = input(f"Выберите тип игрока N{self.number} (ai/hu): ")
        if player_type not in types:
            print("Некорректный тип игрока!")
            return
        elif player_type == "ai":
            player_name = random.choice(player_names)
        else:
            player_name = input(f"Введите имя игрока N{self.number}: ")
        self.name = player_name
        self.type_player = player_type
        self.card = card

    def show_info(self):
        return self.card.show_card(self.name, self.type_player)

    @staticmethod
    def get_index(arr: list, number: int):
        for idx, item in enumerate(arr):
            if number == item:
                return idx

    def check_hu(self, num_check: int, answer: str):
        checked = False
        for iter_index in range(3):
            if num_check in self.card.card_items[iter_index]:
                index = self.get_index(self.card.card_items[iter_index], num_check)
                self.card.card_items[iter_index][index] = '*'
                self.count_checked_items += 1
                checked = True
        if self.count_checked_items == 15:
            return f"winner {self.name}"
        if checked:
            return "to be" if answer == 'y' else f"loser {self.name}"
        else:
            return "to be" if answer == 'n' else f"loser {self.name}"

    def check_ai(self, num_check: int):
        for iter_index in range(3):
            if num_check in self.card.card_items[iter_index]:
                index = self.get_index(self.card.card_items[iter_index], num_check)
                self.card.card_items[iter_index][index] = '*'
                self.count_checked_items += 1
        if self.count_checked_items == 15:
            return f"winner {self.name}"
        return "to be"


if __name__ == '__main__':
    pass
