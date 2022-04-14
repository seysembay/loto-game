import random


class Barrel:

    def __init__(self):
        data = list(range(1, 21))
        random.shuffle(data)
        self.data = data
        self.used = []
        self.counter = 0

    def __len__(self):
        return len(self.used)

    def get_next_val(self):
        if self.counter <= 90:
            tmp = self.data[0]
            self.counter += 1
            self.used.append(self.data[0])
            self.data.pop(0)
            return tmp
        else:
            print("Game over")

    def __str__(self):
        return f"{self.used} {self.counter}"


if __name__ == '__main__':
    test = Barrel()
    print(len(test))
    test.get_next_val()
    test.get_next_val()
    test.get_next_val()
    test.get_next_val()
    test.get_next_val()
    print(len(test))


