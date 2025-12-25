#2.1.1
def greet(name):
    return ('Здравствуйте,', name)
name1 = str(input('Введите ваше имя: '))
print(greet(name1))

#2.1.2
def square(number):
    return number**2
num = int(input('Введите число: '))
print('Квадрат чила:', square(num))

#2.1.3
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
x = int(input('Введете первое число: '))
y = int(input('Введите второе число: '))
print('Большее число:', max_of_two(x, y))