
import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(name):
    try:
        os.mkdir(name)
        print('Папка успешно создана.')
    except FileExistsError:
        #print('{} уже существует'.format(name))
        print('Невозможно создать папку.')

def remove_dir(name):
    try:
        os.rmdir(name)
        print('Папка успешно удалена.')
    except FileNotFoundError:
        #print('{} не существует'.format(name))
        print('Невозможно удалить папку.')

name = [('dir_' + str(i + 1)) for  i in range(9)]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)

main_path = os.getcwd()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, copy_file):
    shutil.copy(first_file, copy_file)