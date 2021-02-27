class PearsBasket:
    pears_amount = 0

    def __init__(self, pears_amount):
        self.pears_amount = int(pears_amount)

    def __add__(self, other):  # +
        """складываются две корзинки, получается новая корзина"""
        return PearsBasket(self.pears_amount + int(other.pears_amount)).pears_amount

    def __sub__(self, other):  # -
        """число вычитается из корзинки, если там есть такое количество груш; если нет – вычитается сколько есть,
        остается 0"""
        pears_amount = int(self.pears_amount)

        if pears_amount > other:
            self.pears_amount -= other
        else:
            self.pears_amount = 0

    def __mod__(self, other):  # %
        """получение остатка от деления, возвращает число: остаток от деления"""
        pears_amount = int(self.pears_amount)
        other = int(other)

        return pears_amount % other

    def __floordiv__(self, other):  # //
        """деление нацело, возвращает список объектов класса со значениями количества груш в каждой корзинке,
        если есть остаток – он должен находиться в дополнительной последней корзинке"""
        baskets = []

        pears_amount = int(self.pears_amount)
        other = int(other)

        amount = pears_amount // other
        remaining = pears_amount % other

        for i in range(amount):
            baskets.append(PearsBasket(amount))

        if remaining:
            baskets.append(PearsBasket(remaining))

        return baskets

    def __str__(self):
        return self.pears_amount

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.pears_amount)
