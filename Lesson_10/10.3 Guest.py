name = str(input('Hello! \nWhat is your name?'))

filename = 'C:/Users/1/PycharmProjects/guest.txt'
with open(filename, 'a') as file_object:
    file_object.write(f'{name}\n')
    file_object.write(f'{name}\n')
