filename = 'C:/Users/1/PycharmProjects/poll.txt'
with open(filename, 'a') as object_file:
    while True:
        reason = str(input('Why do you like programming?'))
        if reason == 'q':
            break
        object_file.write(f'{reason}\n')
