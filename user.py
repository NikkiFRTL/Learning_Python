class User:

    def __init__(self, name, age, administrator=False):
        self.name = name
        self.age = age
        self.administrator = administrator

    def describe_user(self):
        print(self.name, self.age)