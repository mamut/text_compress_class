import gzip
import bz2

class CompressMethodsIterator:

    def __init__(self, path):
        self.path = path
        self.compressors = self._compressors()

    def iterate(self):
        for compressor in self._compressors():
            with compressor() as buffer:
                yield buffer

    def _compressors(self):
        return [
            self._gzipper(),
            self._bzipper()
        ]

    def _gzipper(self):
        return lambda: gzip.open(self.path + '.gz', 'wb')

    def _bzipper(self):
        return lambda: bz2.BZ2File(self.path + '.bz2', 'w')
