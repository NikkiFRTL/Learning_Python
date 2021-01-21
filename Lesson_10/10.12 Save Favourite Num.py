import json


def dump_number():
    number = input('What is your favourite number?\n')
    filename = 'fav_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def load_number():
    filename = 'fav_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def fav_number():
    number = load_number()
    if number:
        print(f'Your number is {number} !')
    else:
        number = dump_number()
        print(f'I see, it is {number}')


fav_number()