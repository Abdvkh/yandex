class Robot:
    positions = []

    directions = {
        'N': 'up',
        'S': 'down',
        'E': 'right',
        'W': 'left'
    }

    MAX_X = 100
    MIN_X = 0
    MAX_Y = 100
    MIN_Y = 0

    def __init__(self, position=(0, 0)):
        self.x = position[0]
        self.y = position[1]

        self.add_path(position[0], position[1])

    def move(self, directions=''):
        """Moves self to the given directions"""
        for direction in directions:
            self.change_position(direction)

        return self.positions[-1]

    def path(self):
        """Passed positions"""
        return self.positions

    def change_position(self, direction):
        """Change current position"""
        where = self.directions[direction]
        self.go(where)

    def go(self, direction):
        """Changes current position regarding provided direction"""
        if direction == 'up':
            self.y = self.y + 1
        elif direction == 'down':
            self.y = self.y - 1
        elif direction == 'right':
            self.x = self.x + 1
        elif direction == 'left':
            self.x = self.x - 1

        self.add_path(self.x, self.y)

    def add_path(self, x, y):
        position = (self.x, self.y)

        is_x_valid = self.MIN_X <= self.x <= self.MAX_X
        is_y_valid = self.MIN_Y <= self.y <= self.MAX_Y

        if is_x_valid and is_y_valid:
            self.positions.append(position)
