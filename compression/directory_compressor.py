from . import BatchCompressor
from utils import files_in_dir


class DirectoryCompressor:

    def __init__(self, path):
        self.path = path

    def compress(self):
        list_of_files = files_in_dir(self.path)
        compressor = BatchCompressor(list_of_files)
        compressor.compress(self.path)
