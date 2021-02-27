from solution import PearsBasket

pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
pb - 2
print([pb])


"""
1/5 passed test

[PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(4), PearsBasket(1)]
30
2
[PearsBasket(15)]
"""