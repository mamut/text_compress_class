#!/usr/bin/env python
# -*- coding: utf-8 -*-

import args
import compression


class Main:

    def datasets(self, path):
        with open(path) as datasets:
            return [dataset.strip() for dataset in datasets.readlines()]

    def __init__(self):
        self.parser = args.Parser()

    def run(self):
        options = self.parser.options()
        if options.compress_datasets and not options.sample_file:
            datasets = self.datasets(options.compress_datasets)
            self.prepare_datasets(datasets)
        elif options.compress_datasets and options.sample_file:
            datasets = self.datasets(options.compress_datasets)
            self.classify_file(options.sample_file, datasets)
        else:
            self.parser.print_help()

    def prepare_datasets(self, data_sets):
        for set in data_sets:
            compression.DirectoryCompressor(set).compress()

    def classify_file(self, filename, datasets):
        for dataset in datasets:
            compressor = compression.AppendingCompressor(filename, dataset)
            compressor.compress()


if __name__ == '__main__':
    Main().run()
