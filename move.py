import os, shutil


def move(start_dir, finish_dir):
    """Перемещение файлов"""
    move = shutil.move(start_dir, os.path.join(finish_dir))


move("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")