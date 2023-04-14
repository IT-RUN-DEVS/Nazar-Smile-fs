import os

def list(dir):
    """Показать все файлы в дирректории"""
    content = os.listdir(dir)
    print(content)



list('/home/n/Рабочий стол/IT_RUN')