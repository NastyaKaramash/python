import os
import shutil
import sys
#Задача1
def make_dir(name):
    try:
        str(os.mkdir(name))
        print('Директория создана')
    except FileExistsError:
        print('Такая дериктория уже существует')

def remove_dir(name):
    try:
        os.removedirs(name)
        print('Директория удалена')
    except FileNotFoundError:
        print('Такой папки не существует')

if __name__ == '__main__':
    for i in range(1,10):
        make_dir(str(i))
    for i in range(1,10):
        remove_dir(str(i))
#Задача2
def list_dir(path):
    for _ in os.listdir(path):
        print(_)
path = os.getcwd()
#Задача3
def copy_file(file, file_copy):
    shutil.copy(file, file_copy)
    print('Копия создана')

if __name__ == '__main__':
    file = sys.argv[0]
    file_copy = file + '.copy'
    copy_file(file, file_copy)
#function for normal
def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Перешел в дерикторию')
    except:
        print('Такой дериктории нет')