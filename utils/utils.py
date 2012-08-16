import os

def files_in_dir(dirpath):
    return (os.path.join(dirpath, file) for file in os.listdir(dirpath))
