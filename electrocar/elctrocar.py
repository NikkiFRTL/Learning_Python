from car.car import Car


class ElectroCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_power = Battery()

    def get_range(self):
        return self.battery_power.power * 120


class Battery:

    def __init__(self, power=75):
        self.power = power

    def upgrade_battery(self):
        if self.power != 100:
            self.power = 100