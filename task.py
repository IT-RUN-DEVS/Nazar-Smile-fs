import os, shutil


# Функция создания нового файла (create).
def create(filename):
    """Создание файлов"""
    try:
        with open(filename, 'w'):
            pass  # Создаем новый файл и немедленно закрываем его
        print(f"Файл {filename} успешно создан")
    except IOError:
        print(f"Не удалось создать файл {filename}")


create('new_file.txt')


# Функция вывода списка файлов и директорий (list).
def list(dir):
    """Показать все файлы в дирректории"""
    content = os.listdir(dir)
    for c in content:
        print(c)


list('/home/n/Рабочий стол/IT_RUN')


# Функция копирования файла (copy).
def copy(start_dir, finish_dir):
    """Копирование файлов"""
    copy = shutil.copy2(start_dir, os.path.join(finish_dir))
    print(f'Файлы из папки {start_dir} скопированы в следующую дирректорию {finish_dir}')


copy("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")


# Функция перемещения файла (move).
def move(start_dir, finish_dir):
    """Перемещение файлов"""
    move = shutil.move(start_dir, os.path.join(finish_dir))
    print(f"Файлы из дирректории {start_dir} перемещены в дирректорию {finish_dir}")


move("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")


# ▪️Написать функцию инициализации новой файловой системы (init).
def init(path='.'):
    init_dir_path = os.path.join(os.getcwd(), '.init')  #создаем путь для директории .init
    if os.path.exists(os.path.join(path, '.init')):
        print(f'Директория инициализации {init_dir_path} уже существует.')
    else:
        os.mkdir(os.path.join(os.getcwd(), '.init'))
        print(f'Директория инициализации {init_dir_path} успешно создана.')


# Функция создания снимка файловой системы (snapshot).
def snapshot(directory='.'):
    # Создаем папку "snapshot", если ее нет
    snapshot_dir = os.path.join(directory, "snapshot")
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)
    # Получаем список файлов и подкаталогов в указанной директории
    file_list = os.listdir(directory)
    # Создаем пустой словарь для хранения информации о файлах и подкаталогах
    snapshot_dict = {}

    # Для каждого элемента в списке файлов и подкаталогов
    for item in file_list:
        # Получаем полный путь к элементу
        item_path = os.path.join(directory, item)
        # Создаем временный словарь, в которую записывается данные в файле
        temp_dict = {}
        # Если элемент является папкой, и его имя не равно "snapshot"
        if os.path.isdir(item_path) and item != "snapshot":
            # Создаем рекурсивный вызов функции snapshot
            snapshot_dict[item] = snapshot(item_path)
            # Если элемент является файлом, и он не находится в папке "snapshot"
        elif os.path.isfile(item_path) and not os.path.samefile(os.path.dirname(item_path),
                                                                os.path.join(directory, "snapshot")):
            # Записываем его имя в словарь
            with open(item, 'r') as f:
                # Читаем все строки файла
                lines = f.readlines()
            for i, line in enumerate(lines):
                # Убираем символы переноса строки и лишние пробелы в начале и конце строки
                line = line.strip()
                # Добавляем строку в словарь
                temp_dict[i + 1] = line

        snapshot_dict[item] = temp_dict
    # Создаем имя файла с датой
    filename = 'snapshot_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.json'

    # Создаем файл и записываем в него словарь в формате JSON
    with open(os.path.join(snapshot_dir, filename), 'w', encoding="utf-8") as f:
        json.dump(snapshot_dict, f, indent=4, ensure_ascii=False)
    print(snapshot_dict)


# Функция создания резервной копии всей файловой системы (backup).
def backup(source_folder, backup_folder):
    """
    Создает бэкап папки source_folder и сохраняет его в папку backup_folder.
    """
    shutil.copytree(source_folder, backup_folder)
    print(f"Бэкап папки {source_folder} успешно создан и сохранен в {backup_folder}.")


backup("/home/n/Рабочий стол/IT_RUN", "/home/n/Рабочий стол/IT_RUN/backup")








