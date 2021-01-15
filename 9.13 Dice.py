from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, throws):
        for i in range(throws):
            print(randint(1, self.sides))


dice = Dice(10)
dice.roll_die(10)
