import os

def files_in_dir(dirpath):
    return [os.path.join(dirpath, file) for file in os.listdir(dirpath)]

def temp_archive_filename(testfile, dataset):
    base = testfile.split('.')[0]
    ext = dataset.split('/')[-1]
    return "{0}_{1}".format(base, ext)
