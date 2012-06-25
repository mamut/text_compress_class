#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gzip
import bz2
import argparse

config = {
    'datasets':
    ['datasets/austen', 'datasets/dickens', 'datasets/doyle', 'datasets/twain']
}


class DirCompressor:

    def __init__(self, path):
        self.path = path

    def implementations(self):
        compressors = [self.gzipper(), self.bzipper()]
        for compressor in compressors:
            with compressor() as buffer:
                yield buffer

    def gzipper(self):
        return lambda: gzip.open(self.path + '.gz', 'wb')

    def bzipper(self):
        return lambda: bz2.BZ2File(self.path + '.bz2', 'w')


class Main:

    def parser(self):
        parser = argparse.ArgumentParser(
            description="compression based text classification experiment")
        parser.add_argument('-c', '--compress',
                            action='store_true',
                            help="prepare reference datasets")
        parser.add_argument('-l', '--classify',
                            action='store',
                            help="classify given text")
        return parser

    def extract_options(self):
        return self.parser().parse_args()

    def run(self):
        options = self.extract_options()
        if options.compress:
            self.prepare_datasets(config['datasets'])
        elif options.classify:
            self.classify_file(options.classify)
        else:
            self.parser().print_help()

    def prepare_datasets(self, data_sets):
        for set in data_sets:
            self.compress_dir(set)

    def classify_file(self, filename):
        print filename

    def compress_dir(self, path):
        data = self.dir_contents(path)
        for file in DirCompressor(path).implementations():
            file.write(data)

    def dir_contents(self, dirpath):
        contents = []
        for file in self.files_in_dir(dirpath):
            contents.append(self.read_all(file))
        return '\n'.join(contents)

    def files_in_dir(self, path):
        return (os.path.join(path, file) for file in os.listdir(path))

    def read_all(self, file):
        print file
        with open(file) as file:
            return file.read()


if __name__ == '__main__':
    Main().run()
