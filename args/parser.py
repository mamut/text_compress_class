import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="compression based text classification experiment")

        self.parser.add_argument('-c', '--compress',
                            action='store_true',
                            help="prepare reference datasets")

        self.parser.add_argument('-l', '--classify',
                            action='store',
                            help="classify given text")

    def options(self):
        return self.parser.parse_args()

    def print_help(self):
        self.parser.print_help()
