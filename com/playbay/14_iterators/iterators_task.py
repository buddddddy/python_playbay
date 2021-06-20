from random import randrange


class RandomNumbers:

    def __init__(self, quantity, min, max):
        self.qty = quantity
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return randrange(self.min, self.max)
        else:
            raise StopIteration


first = RandomNumbers(10, 0, 50)

for i in first:
    print(i)
