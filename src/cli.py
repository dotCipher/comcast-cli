#!/usr/bin/env python2

import os
import argparse

DIR_SOURCE = os.path.dirname(os.path.abspath(__file__))
DIR_PROJECT_ROOT = os.path.normpath(os.path.join(DIR_SOURCE, '..'))


class ComcastCLI:

    CMD_DATA = 'data'

    ARG_VERBOSE = 'verbose'

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Pull metrics from the Comcast data services via CLI")
        # self.parser.add_argument(self.CMD_DATA,
        #                          dest=self.CMD_DATA,
        #                          default=False,
        #                          action='store_true',
        #                          help='Scrapes the Comcast website for data usage metrics')
        self.parser.add_argument('--' + self.ARG_VERBOSE,
                                 '-' + self.ARG_VERBOSE[0],
                                 default=0,
                                 action='count',
                                 help='Increase level of verbosity for output logging')
        self.args = vars(self.parser.parse_args())

    def print_help(self, output=None):
        self.parser.print_help(file=output)

    def is_any_set(self):
        for value in self.args.values():
            if value is not False and value is not None:
                return True
        return False

    def _is_set(self, arg):
        return self.args[arg]

    def is_data_set(self):
        return self._is_set(self.CMD_DATA)


def main():
    cli = ComcastCLI()

    if not cli.is_any_set():
        cli.print_help()
        return -1

    return 0

if __name__ == "__main__":
    main()
