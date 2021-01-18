enter_number1 = input()
enter_number2 = input()

try:
    first_number = int(enter_number1)
    second_number = int(enter_number2)
except ValueError:
    print('Please, enter only numbers!')
else:
    print(first_number + second_number)
