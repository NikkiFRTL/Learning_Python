filename = 'C:/Users/1/PycharmProjects/guest_book.txt'
with open(filename, 'a') as object_file:
    while True:
        name = str(input('What is your name?'))
        if name == 'q':
            break
        print(f'Hello, {name}')
        object_file.write(f'{name}\n')
