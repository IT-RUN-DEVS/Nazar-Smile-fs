import os, shutil, sys, zipfile
from datetime import datetime


def create(file_name=None, file_content=None):
    """Функция для создания нового файла (create)"""
    if not file_name:
        file_name = input('Введите название файла, который Вы хотите создать: ')
    if os.path.exists(file_name):
        return f'Файл с таким названием уже существует!'
    else:
        if not file_content:
            file_content = input('Введите текст в этот файл: ')
        with open(file_name, 'w') as f:
            f.write(file_content)


def list(dir=None):
    """Функция для вывода списка файлов и дирректорий (list)"""
    content = os.listdir(dir)  # Получаем список файлов в текущей директории
    for c in content:
        print(c)


def copy(start_dir=None, finish_dir=None):
    """Функция для копирования файла (copy)"""
    if start_dir is None:
        start_dir = input('Введите название файла для копирования: ')
        if not start_dir:
            return f'Вы не ввели название файла'
    if start_dir not in os.listdir('.'):
        return f'Файла {start_dir} В текущей директории нет'
    if finish_dir is None:
        name = start_dir.split('.')
        finish_dir = name[0] + '_copy.' + name[1] # Cоздаем новый файл добавляя в текущее название _copy
        shutil.copy2(start_dir, os.path.join(finish_dir))
        print(f'Файлы из папки {start_dir} скопированы в следующую директорию {finish_dir}')

def move(filename=None, directory=None):
    """Функция перемещения файла (move)"""
    if filename is None:
        filename = input('Введите название файла, для перемещения:')
    if directory is None:
        directory = input('Введите путь, куда нужно переместить указанный файл:')

    if not os.path.isfile(filename): # Проверяем, существует ли указанный файл в текущей дирректории
        print(f"Файл '{filename}' не найден в текущей директории.")
        return
    if not os.path.isdir(directory): # Проверяем, существует ли указанная дирректория
        print(f"Директория '{directory}' не найдена.")
        return

    destination = os.path.join(directory, os.path.basename(filename)) # Создаем путь для перемещения файла

    if os.path.isfile(destination): # Проверяем, существует ли уже файл с таким именем в указанной директории
        print(f"Файл '{os.path.basename(filename)}' уже существует в директории '{directory}'.")
        return

    shutil.move(filename, destination) # Перемещаем файл в указанную директорию
    print(f"Файл '{filename}' успешно перемещен в директорию'{directory}'.")


def init(path='.'):
    """Функция для инициализации новой файловой системы (init)"""
    init_dir_path = os.path.join(os.getcwd(), '.init')  # Cоздаем путь для директории .init
    if os.path.exists(os.path.join(path, '.init')):
        print(f'Директория инициализации {init_dir_path} уже существует.')
    else:
        os.mkdir(os.path.join(os.getcwd(), '.init'))
        print(f'Директория инициализации {init_dir_path} успешно создана.')


def backup(directory=None):
    """Функция для создания резервной копии всей файловой системы (backup)"""
    if directory is None: # Если директория не задана
        directory = input("Введите путь к директории: ")

    ignore_files = ["backup", ".git", ""]  # Игнор лист, чтобы функция рекурсивно не сохраняла папку backup

    if not os.path.isdir(directory): # Проверяем правильность введенной директории
        print(f"{directory} не является директорией")
        return

    backup_folder = os.path.join(directory, "backup") # Если нет папки backup, то создаём её
    if os.path.exists(backup_folder):
        print("Папка backup уже существует")
        return
    os.mkdir(backup_folder)

    # Формируем название файла backup, он будет состоять из времени, когда был сделан
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_folder, f"backup_{current_time}.zip")

    with zipfile.ZipFile(backup_file, "w", compression=zipfile.ZIP_DEFLATED) as backup_zip: # Создаем файл zip и пишем во внутрь содержимого внутри введенной директории
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                if file_path in ignore_files:
                    continue
                if os.path.abspath(file_path).startswith(os.path.abspath(backup_folder)):
                    continue
                backup_zip.write(file_path, os.path.relpath(file_path, directory))

    print(f"Резервное копирование успешно создано в папке 'backup' с названием {backup_file}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        function_name = sys.argv[1]
        if function_name == 'create':
            create()
        elif function_name == 'list':
            list()
        elif function_name == 'copy':
            copy()
        elif function_name == 'move':
            move()
        elif function_name == 'init':
            init()
        elif function_name == 'backup':
            backup()
        else:
            print(f'Unknown function: {function_name}')



