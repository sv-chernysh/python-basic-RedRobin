class Vehicle:
    def __int__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print("Speed increased")

    def break_speed(self):
        print("Speed decreased")

    def mileage_info(self):
        print("Mileage:", self.mileage)