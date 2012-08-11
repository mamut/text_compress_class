import os
import gzip
import bz2


class DirectoryCompressor:

    def __init__(self, path):
        self.path = path

    def implementations(self):
        compressors = [self.gzipper(), self.bzipper()]
        for compressor in compressors:
            with compressor() as buffer:
                yield buffer

    def gzipper(self):
        return lambda: gzip.open(self.path + '.gz', 'wb')

    def bzipper(self):
        return lambda: bz2.BZ2File(self.path + '.bz2', 'w')

    def compress(self):
        data = self.dir_contents()
        for file in self.implementations():
            file.write(data)

    def dir_contents(self):
        contents = []
        for file in self.files_in_dir():
            contents.append(self.read_all(file))
        return "\n".join(contents)

    def files_in_dir(self):
        return (os.path.join(self.path, file)
                for file in os.listdir(self.path))

    def read_all(self, file):
        print file
        with open(file) as file:
            return file.read()
