def read_txt(txt):
    try:
        with open(txt, 'r', encoding='utf-8') as object_file:
            contents = object_file.read().split()
    except FileNotFoundError:
        pass
    else:
        print(*contents)


cats = 'C:/Users/1/PycharmProjects/cats.txt'
dogs = 'C:/Users/1/PycharmProjects/dogs.txt'
animals = [cats, dogs]
for file in animals:
    read_txt(file)
