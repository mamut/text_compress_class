import os

from . import BatchCompressor


class DirectoryCompressor:

    def __init__(self, path):
        self.path = path

    def compress(self):
        list_of_files = self._files_in_dir()
        compressor = BatchCompressor(list_of_files)
        compressor.compress(self.path)

    def _files_in_dir(self):
        return (os.path.join(self.path, file)
                for file in os.listdir(self.path))
