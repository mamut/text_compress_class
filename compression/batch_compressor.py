from . import CompressMethodsIterator


class BatchCompressor:

    def __init__(self, files):
        self.files = files

    def compress(self, out_path):
        data = self._compile_files()
        for file in self._implementations(out_path):
            file.write(data)

    def _compile_files(self):
        contents = []
        for file in self.files:
            contents.append(self._read_all(file))
        return "\n".join(contents)

    def _read_all(self, filepath):
        print filepath
        with open(filepath) as file:
            return file.read()

    def _implementations(self, out_path):
        for compressor in CompressMethodsIterator(out_path):
            with compressor() as buffer:
                yield buffer
