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


class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def description(self):
        print(self.name, self.cuisine)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def nullifier(self):
        self.number_served = 0


class IceCreamServe(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = {'choco': 1, 'banana': 2, 'strawberry': 3}

    def icecream_menu(self):
        print(*self.flavors)


class User:

    def __init__(self, name, age, administrator=False):
        self.name = name
        self.age = age
        self.administrator = administrator

    def describe_user(self):
        print(self.name, self.age)


class Admin(User):

    def __init__(self, name, age, administrator=False):
        super().__init__(name, age, administrator)
        self.privileges = Privileges().show_rights()

    def show_privileges(self):
        if self.administrator:
            print(self.name, self.age, self.privileges)
        else:
            print(self.name, self.age)


class Privileges:

    def __init__(self):
        self.rights = ['Разрешено добавлять сообщения',
                       'Разрешено удалять пользователей',
                       'Разрешено банить пользователей']

    def show_rights(self):
        return self.rights


my_car = ElectroCar('tesla', 'type S', 2020)
print(my_car.get_range())
my_car.battery_power.upgrade_battery()
print(my_car.get_range())
