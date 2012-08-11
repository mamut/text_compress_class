#!/usr/bin/env python
# -*- coding: utf-8 -*-

import args
import compression

config = {
    'datasets':
    ['datasets/austen', 'datasets/dickens', 'datasets/doyle', 'datasets/twain']
}


class Main:

    def __init__(self):
        self.parser = args.Parser()

    def run(self):
        options = self.parser.options()
        if options.compress:
            self.prepare_datasets(config['datasets'])
        elif options.classify:
            self.classify_file(options.classify)
        else:
            self.parser.print_help()

    def prepare_datasets(self, data_sets):
        for set in data_sets:
            compression.DirectoryCompressor(set).compress()

    def classify_file(self, filename):
        print filename


if __name__ == '__main__':
    Main().run()
