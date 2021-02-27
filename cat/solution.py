class AbstractCat:
    weight = 0
    food = 0
    remaining_food = 0
    MAX_WEIGHT = 100

    def eat(self, food_amount=0):
        self.food += food_amount + self.remaining_food
        remaining = self.food % 10

        if remaining == 0 or self.food > 10:
            self.remaining_food += remaining

            self.weight += self.food // 10
            self.food -= self.food
        else:
            self.remaining_food = remaining

    def __repr__(self):
        return "{} ({})".format(self.__class__.__name__, self.weight)


class Kitten(AbstractCat):
    def __init__(self, weight):
        self.weight = weight

    def meow(self):
        return 'meow...'

    def sleep(self):
        return 'Snore' * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return 'MEOW...'

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it!'
