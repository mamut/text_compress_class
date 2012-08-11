import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="compression based text classification experiment")

        self.parser.add_argument('-c', '--compress_datasets',
                            action='store',
                            help="prepare reference datasets")

        self.parser.add_argument('-t', '--sample_file',
                            action='store',
                            help="classify given text")

    def options(self):
        return self.parser.parse_args()

    def print_help(self):
        self.parser.print_help()
