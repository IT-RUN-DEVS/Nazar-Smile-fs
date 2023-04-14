import os, shutil

def copy(start_dir, finish_dir):
    """Копирование файлов"""
    copy = shutil.copy2(start_dir, os.path.join(finish_dir))


copy("/home/n/Рабочий стол/IT_RUN/folder_test/test.py", "/home/n/Рабочий стол/IT_RUN")