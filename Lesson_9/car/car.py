class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 10

    def description(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def odometre(self):
        print(f'My car has {self.odometr_reading} km on it')

    def update_odometr(self, km):
        if km >= self.odometr_reading:
            self.odometr_reading = km
        else:
            print(f"Don't cheat, you bastard!")

    def increament_odometr(self, km):
        self.odometr_reading += km