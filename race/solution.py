class Transport:

    def __init__(self, identity, speed, fuel_type=None):
        self.id = identity
        self.speed = speed
        if fuel_type:
            self.fuel_type = fuel_type

    def distance_till_finish(self, track_length, time):
        passed_distance = int(self.speed) * int(time)
        remaining_distance = int(track_length) - int(passed_distance)
        return remaining_distance


class Car(Transport):
    FUEL_AFFECT = {
        '98': 0,
        '95': 0.1,
        '92': 0.2
    }

    def __init__(self, identity, speed, fuel_type):
        super().__init__(identity, speed, fuel_type)
        speed = int(speed)
        self.speed = speed - (speed * self.FUEL_AFFECT[fuel_type])


class Cart(Transport):
    FUEL_AFFECT = {
        '98': 0,
        '95': 0,
        '92': 0
    }

    def __init__(self, identity, speed, fuel_type):
        super().__init__(identity, speed, fuel_type)
        self.speed = int(speed) - (int(speed) * self.FUEL_AFFECT[fuel_type])


class Motorcycle(Transport):
    FUEL_AFFECT = {
        '98': 0,
        '95': 0.2,
        '92': 0.4
    }

    def __init__(self, identity, speed, fuel_type):
        super().__init__(identity, speed, fuel_type)
        self.speed = int(speed) - (int(speed) * self.FUEL_AFFECT[fuel_type])


if __name__ == '__main__':
    """1/2 passed test"""

    participants = []

    types = {
        '1': 'CAR',
        '2': 'MOTORCYCLE',
        '3': 'CART'
    }

    data = input('')
    lines_amount, track_length, time = data.split(' ')

    for _ in range(int(lines_amount)):
        transportation = None

        data = input('').split(' ')
        if len(data) == 4:
            transport_fuel_type = data[3]
        transport_id = data[0]
        transport_type = data[1]
        transport_speed = data[2]

        if types[transport_type] == 'CAR':
            transportation = Car(transport_id, transport_speed, transport_fuel_type)
        if types[transport_type] == 'CART':
            transportation = Cart(transport_id, transport_speed, transport_fuel_type)
        if types[transport_type] == 'MOTORCYCLE':
            transportation = Motorcycle(transport_id, transport_speed, transport_fuel_type)

        participants.append(transportation)

    distances = [participant.distance_till_finish(track_length, time) for participant in participants]
    closest = min(distances)
    closest = [p for p in participants if p.distance_till_finish(track_length, time) == closest]
    print(closest[0].id)
