def describe_person(name, age=30):
    return ('Имя человека:', name, ', Возраст:', age)
name1 = str(input('Введите имя: '))
age = input('Введите возраст (или пропустите для авто-заполнения): ')
if age == '':
    print (describe_person(name1))
else:
    print(describe_person(name1, int(age)))