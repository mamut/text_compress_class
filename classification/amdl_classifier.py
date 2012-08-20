import os

from utils import temp_archive_filename


class AMDLClassifier:

    def __init__(self, testfile, datasets):
        print testfile
        self.testfile = testfile
        self.datasets = datasets

    def calculate(self):
        results = []
        for dataset in self.datasets:
            fit_values = self._calculate_fit_values(dataset)
            result = (dataset, fit_values)
            results.append(result)
        return tuple(results)

    def _calculate_fit_values(self, dataset):
        fit_values = []
        for ext in self._compression_methods():
            fit_value = self._calculate_fit_value(ext, dataset)
            fit_values.append((ext, fit_value))
        return tuple(fit_values)

    def _calculate_fit_value(self, ext, dataset):
        orig_dataset_path = "{0}.{1}".format(dataset, ext)
        testfile_dataset_path_base = temp_archive_filename(
                self.testfile, dataset)
        testfile_dataset_path = "{0}.{1}".format(
                testfile_dataset_path_base, ext)
        print testfile_dataset_path
        orig_dataset_size = os.path.getsize(orig_dataset_path)
        testfile_dataset_size = os.path.getsize(testfile_dataset_path)
        return testfile_dataset_size - orig_dataset_size

    def _compression_methods(self):
        return (
            'gz',
            'bz2',
            'rar'
        )
