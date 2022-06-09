import random

class Die():
    def __init__(self):
        self.val = 0
        self.points = 0

    def randNumber(self):
        self.val = random.randint(1, 5)
        if self.val == 1:
            self.points = 100
        elif self.val == 5:
            self.points = 50
