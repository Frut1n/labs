class UserAccount:
    def init(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return f"Пароль успешно изменен"

    def check_password(self, password):
        return password == self.__password

    def get_account_info(self):
        return f"Username: {self.username}, Email: {self.email} Password: {self.__password}"


user1 = UserAccount("Valya", "dot@gmail.com", "qwerty123")

password_input = input("Задайте новый пароль: ")
user1.set_password(password_input)

user_input = input("Введите пароль для проверки: ")
if user1.check_password(user_input):
    print("Пароль верный")
else:
    print("Неверный пароль")
print(user1.get_account_info())

print(user1.__password)