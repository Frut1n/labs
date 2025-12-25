def write_new_file(namefile, content):
    with open(namefile, 'w') as file:
        file.write(content)
    print("Текст записан в файл", namefile)


def append_in_file(namefile, content):
    with open(namefile, 'a') as file:
        file.write(content)
        print("Текст добавлен в файл", namefile)


user_text = input('Введите текст для запсии в новый файл:')
write_new_file('user_input.txt', user_text)

user_add = input("Введите текст для добавления в существующий файл: ")
append_in_file('user_input.txt', user_add)
