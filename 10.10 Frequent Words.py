
def count_words(file):
    try:
        with open(file) as object_file:
            contents = object_file.read()
    except FileNotFoundError:
        print("File doesn't exist")
    else:
        print(contents.lower().count('the '))


secrets = 'C:/Users/1/PycharmProjects/Harry Potter and the chamber of secrets.txt'
sorcerer = "C:/Users/1/PycharmProjects/Harry Potter and the sorcerer's stone.txt"
books = [secrets, sorcerer]
for book in books:
    count_words(book)
