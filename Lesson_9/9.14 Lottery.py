from random import choice


random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']


def lottery(numbers):
    win_number = ''
    for i in range(4):
        win_number += str(choice(numbers))
    return f'Winning number is {win_number}'


print(lottery(random_list))