import os
import shutil
import sys
import easy5

answer = ''
while answer != 'Q':
    answer = input('Для работы введите W, для выхода Q: ')
    if answer == 'W':
        print('[1] перейти в папку')
        print('[2] посмотреть содержимое текущей папки')
        print('[3] удалить папку')
        print('[4] создать папку')
        do = int(input('Укажите номер действия: '))

        if do == 1:
            dir_name = input ('Введите путь к папке: ')
            easy5.change_dir(dir_name)
        elif do == 2:
            dir_name = os.getcwd()
            easy5.list_dir(dir_name)
        elif do == 3:
            dir_name = input('Введите путь до папки, которую надо удалить: ')
            easy5.remove_dir(dir_name)
        elif do == 4:
            dir_name == input('Введите путь до папки, которую хотите создать: ')
            easy5.make_dir(dir_name)
        else:
            pass


