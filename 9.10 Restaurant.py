from restaurant.restaurant import Restaurant


my_restaurant = Restaurant('Bad Bear', 'Russian')
my_restaurant.description()
my_restaurant.set_number_served(15)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(25)
print(my_restaurant.number_served)
my_restaurant.nullifier()
print(my_restaurant.number_served)