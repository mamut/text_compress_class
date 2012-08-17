from . import BatchCompressor
from utils import files_in_dir, temp_archive_filename


class AppendingCompressor:

    def __init__(self, testfile, dataset):
        self.testfile = testfile
        self.dataset = dataset

    def compress(self):
        compressor = BatchCompressor(self._list_of_files())
        outfile = self._result_filename()
        compressor.compress(outfile)

    def _list_of_files(self):
        return list(files_in_dir(self.dataset)) + [self.testfile]

    def _result_filename(self):
        return temp_archive_filename(self.testfile, self.dataset)
