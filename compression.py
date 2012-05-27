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


def prepare_datasets(data_sets):
    for set in data_sets:
        compress_dir(set)


def compress_dir(path):
    data = dir_contents(path)
    gzip_it(data, path + '.gz')
    bz2_it(data, path + '.bz2')


def gzip_it(data, path):
    with gzip.open(path, 'wb') as buffer:
        print path
        buffer.write(data)


def bz2_it(data, path):
    with bz2.BZ2File(path, 'w') as buffer:
        print path
        buffer.write(data)


def dir_contents(dirpath):
    contents = []
    for file in files_in_dir(dirpath):
        contents.append(read_all(file))
    return '\n'.join(contents)


def files_in_dir(path):
    return (os.path.join(path, file) for file in os.listdir(path))


def read_all(file):
    try:
        print file
        with open(file) as file:
            return file.read()
    except IOError:
        return ""


if __name__ == '__main__':
    if options.compress:
        prepare_datasets(config['datasets'])
