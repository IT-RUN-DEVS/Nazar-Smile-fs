def create(filename):
    """Создание файлов"""
    try:
        with open(filename, 'w'):
            pass  # Создаем новый файл и немедленно закрываем его
        print(f"Файл {filename} успешно создан")
    except IOError:
        print(f"Не удалось создать файл {filename}")



create('new_file.txt')














