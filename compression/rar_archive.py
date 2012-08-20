import os

from librar import archive

class RarArchive:

    def __init__(self, files, out_path):
        self.files = files
        self.out_path = "{0}.{1}".format(out_path, 'rar')

        self.archive = archive.Archive(self.out_path, '.')
        for file in self.files:
            self.archive.add_file(file)

    def compress(self):
        self.archive.run()
