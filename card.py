import random


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


class Card:

    def __init__(self):
        self.card_items = []
        self.positions = []
        data = random.sample(range(1, 90), 15)
        split(data, 3)
        lol = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
        for i in range(3):
            self.positions = lol(data, 5)
        for items in self.positions:
            items.sort()
            for i in range(4):
                random_pos = random.randint(1, 9)
                items.insert(random_pos, '#')
            self.card_items.append(items)

    def __str__(self):
        return f"{self.card_items}"

    def show_card(self):
        print('------------------------------------------')
        for row in self.card_items:
            print(row)
        print('------------------------------------------')

if __name__ == '__main__':
    test = Card()
    test.show_card()
