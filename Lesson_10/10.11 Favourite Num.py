import json


def load_number():
    filename = 'fav_number.json'
    try:
        with open(filename) as object_file:
            number = json.load(object_file)
    except FileNotFoundError:
        return None
    else:
        return number


def dump_number():
    filename = 'fav_number.json'
    number = input(f'What is your number?\n')
    with open(filename, 'w') as object_file:
        json.dump(number, object_file)
    return number


def fav_number():
    number = load_number()
    if number:
        print(f'Your number is {number}!')
    else:
        number = dump_number()
        print(f'Next time I will remember your number {number}')


fav_number()
