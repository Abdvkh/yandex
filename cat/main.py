from solution import *

"""6/8 test passed"""


def first_example():
    abscat = AbstractCat()
    abscat.eat(125)
    abscat.eat(17)
    print(abscat)
    kit = Kitten(21)
    print(kit.sleep())
    cat = Cat(83, 'Molly')
    print(cat.meow())
    print(cat.get_name())


def second_example():
    kit = Kitten(15)
    kit.eat(24)
    print(kit)
    cat = Cat(41, 'Molly')
    print(cat.catch_mice())
    print(cat)


first_example()
second_example()
