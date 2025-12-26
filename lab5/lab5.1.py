class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


book = Book('Харка, сын вождя', 'Лизелотта Вельскопф-Генрих', '1901')
print(book.get_info())