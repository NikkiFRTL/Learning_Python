from random import choice


random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']


def lottery(numbers):
    win = ''
    for i in range(4):
        win += str(choice(numbers))
    return win


win_number = lottery(random_list)


def probability_of_win(ticket):
    winning_number = lottery(random_list)
    event = 0
    while winning_number != ticket:
        winning_number = lottery(random_list)
        event += 1
    return event


def average_win(n):
    average = []
    for i in range(n):
        average.append(probability_of_win('A3E9'))
    return sum(average) / len(average)


my_ticket = 'A3E9'
print(average_win(5))