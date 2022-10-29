class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print("Speed increased")

    def break_speed(self):
        print("Speed decreased")

    def mileage_info(self):
        print("Mileage:", self.mileage)


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity_info):
        super().__init__(max_speed, mileage)
        self.seating_capacity_info = seating_capacity_info

    def seating_capacity(self):
        print(f'Seating capacity: {self.seating_capacity_info} {self.__class__.__name__}')


print(issubclass(Bus, Vehicle))
# ford = Vehicle(120, 8000)
# ford.increase_speed()
# ford.break_speed()
# ford.mileage_info()
#
# bohdan = Bus(100, 2000, 30)
# bohdan.mileage_info()
# bohdan.seating_capacity()