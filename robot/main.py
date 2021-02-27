from solution import Robot

"""3/9 test passed"""

r = Robot((0, 0))
print(r.move('NENW'))  # (0, 2)
print(*r.path())  # (0, 0) (0, 1) (1, 1) (1, 2) (0, 2)

