import os, tarfile

def backup(directory, snapshot_filename):
    """Создание снимка и резервной копии"""
    # Создаем объект TarFile
    with tarfile.open(snapshot_filename, "w:gz") as tar:
        # Добавляем все файлы и поддиректории из директории в архив
        tar.add(directory, arcname=os.path.basename(directory))


backup('/home/n/Рабочий стол/IT_RUN', 'snapshot.tar.gz')