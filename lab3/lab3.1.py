def read_all(file):
    try:
        with open(file, 'r') as file:
            print("Чтение всего файла")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")

def read_lines(file1):
    try:
        with open(file1, 'r') as file:
            print("Построчное чтение")
            line_num = 1
            for line in file:
                print(f"{line_num}: {line}", end='')
                line_num += 1
    except FileNotFoundError:
        print(f"Ошибка: файл '{file1}' не найден.")

type = input("Тип чтения: Полный / Построчный ")
if type=='Полный':
    read_all('example.txt')
elif type=='Построчный':
    read_lines('example.txt')
else:
    print('Неизвестный тип чтения')
