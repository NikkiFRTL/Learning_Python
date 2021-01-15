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

    def null(self):
        self.number_served = 0


class IceCreamServe(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = {'choco': 1, 'banana': 2, 'strawberry': 3}

    def icecream_menu(self):
        print(*self.flavors)
