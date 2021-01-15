from user.user import User


class Admin(User):

    def __init__(self, name, age, administrator=False):
        super().__init__(name, age, administrator)
        self.privileges = Privileges().show_rights()

    def show_privileges(self):
        if self.administrator:
            print(self.name, self.age, self.privileges)
        else:
            print(self.name, self.age)


class Privileges:

    def __init__(self):
        self.rights = ['Разрешено добавлять сообщения',
                       'Разрешено удалять пользователей',
                       'Разрешено банить пользователей']

    def show_rights(self):
        return self.rights
