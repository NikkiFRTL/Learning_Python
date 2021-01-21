
while True:
    enter_number1 = input('Enter the first number\n')
    if enter_number1 == 'q':
        break
    enter_number2 = input('Enter the second number\n')
    if enter_number2 == 'q':
        break
    try:
        first_number = int(enter_number1)
        second_number = int(enter_number2)
    except ValueError:
        print('Please, enter only numbers!')
    else:
        print(first_number + second_number)
