import os, shutil, tarfile


def create(filename):
    """Создание файлов"""
    try:
        with open(filename, 'w'):
            pass  # Создаем новый файл и немедленно закрываем его
        print(f"Файл {filename} успешно создан")
    except IOError:
        print(f"Не удалось создать файл {filename}")



# create('new_file.txt')


def list(dir):
    """Показать все файлы в дирректории"""
    content = os.listdir(dir)
    print(content)



# list('/home/n/Рабочий стол/IT_RUN')


def copy(start_dir, finish_dir):
    """Копирование файлов"""
    copy = shutil.copy2(start_dir, os.path.join(finish_dir))


# copy("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")


def move(start_dir, finish_dir):
    """Перемещение файлов"""
    move = shutil.move(start_dir, os.path.join(finish_dir))


# move("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")


def backup(directory, snapshot_filename):
    """Создание снимка и резервной копии"""
    # Создаем объект TarFile
    with tarfile.open(snapshot_filename, "w:gz") as tar:
        # Добавляем все файлы и поддиректории из директории в архив
        tar.add(directory, arcname=os.path.basename(directory))


backup('/home/n/Рабочий стол/IT_RUN', 'snapshot.tar.gz')


