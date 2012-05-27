#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gzip
import bz2
import argparse

config = {
        'datasets':
            ['datasets/austen', 'datasets/dickens',
                'datasets/doyle', 'datasets/twain']
    }

parser = argparse.ArgumentParser(description="compression based text"
        " classification experiment")
parser.add_argument('-c', '--compress', action='store_true',
        help="prepare reference datasets")
options = parser.parse_args()


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


def prepare_datasets(data_sets):
    for set in data_sets:
        compress_dir(set)


def compress_dir(path):
    data = dir_contents(path)
    for file in DirCompressor(path).implementations():
        file.write(data)


def dir_contents(dirpath):
    contents = []
    for file in files_in_dir(dirpath):
        contents.append(read_all(file))
    return '\n'.join(contents)


def files_in_dir(path):
    return (os.path.join(path, file) for file in os.listdir(path))


def read_all(file):
    print file
    with open(file) as file:
        return file.read()


if __name__ == '__main__':
    if options.compress:
        prepare_datasets(config['datasets'])
