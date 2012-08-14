import gzip
import bz2

class CompressMethodsIterator:

    def __init__(self, path):
        self.path = path
        self.compressors = self._compressors()

    def __iter__(self):
        return self

    def next(self):
        if self.compressors:
            return self.compressors.pop()
        else:
            raise StopIteration

    def _compressors(self):
        return [
            self._gzipper(),
            self._bzipper()
        ]

    def _gzipper(self):
        return lambda: gzip.open(self.path + '.gz', 'wb')

    def _bzipper(self):
        return lambda: bz2.BZ2File(self.path + '.bz2', 'w')
