#Задача1
def func1():
    print(name, age, 'год(а), проживает в городе ', town)
name = input('Введите ваше имя: ')
age = int(input('возраст: '))
town = input ('город проживания ')
func1()
#Задача2
def func2():
    x = max(num1, num2, num3)
    print(x)
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
func2()
#Задача3 здесь не разобралась
def func3():
    maxi = max(str1, str2, str3, key=len)
    print(maxi)
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
str3 = input('Введите третью строку: ')
func3()

def func3(*args):                  # я не разобралась как работает *args
    maxi = max(arg, key=len)       # и почему функция не работает если в скобках написать аргументы
    print(maxi)
func3()

