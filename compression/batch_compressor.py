import gzip
import bz2


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
        compressors = [self._gzipper(out_path), self._bzipper(out_path)]
        for compressor in compressors:
            with compressor() as buffer:
                yield buffer

    def _gzipper(self, path):
        return lambda: gzip.open(path + '.gz', 'wb')

    def _bzipper(self, path):
        return lambda: bz2.BZ2File(path + '.bz2', 'w')
