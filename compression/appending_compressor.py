from . import BatchCompressor
from utils import files_in_dir


class AppendingCompressor:

    def __init__(self, testfile, dataset):
        self.testfile = testfile
        self.dataset = dataset

    def compress(self):
        print self._list_of_files()
        compressor = BatchCompressor(self._list_of_files())
        outfile = self._result_filename()
        print outfile
        compressor.compress(outfile)

    def _list_of_files(self):
        return list(files_in_dir(self.dataset)) + [self.testfile]

    def _result_filename(self):
        base = self.testfile.split('.')[0]
        dataset = self.dataset.split('/')[-1]
        return "{0}_{1}".format(base, dataset)
