import os

from librar import archive

class RarArchive:

    def __init__(self, files, out_path):
        self.files = files
        self.out_path = "{0}.{1}".format(out_path, 'rar')

    def compress(self):
        tempfile = open('tempfile', 'w')
        tempfile.write(self._compile_files())
        tempfile.close()

        self.archive = archive.Archive(self.out_path, '.')
        self.archive.add_file('tempfile')
        self.archive.run()

    def _compile_files(self):
        contents = []
        for file in self.files:
            contents.append(self._read_all(file))
        return "\n".join(contents)

    def _read_all(self, filepath):
        print filepath
        with open(filepath) as file:
            return file.read()
