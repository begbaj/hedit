#!/bin/python3

import os
from sys import argv
#-------------------------------------------------------------------------------
# CONFIGURATION
#-------------------------------------------------------------------------------
HISTORY_FILE = os.path.expanduser('~/.zsh_history')

_HELP = "usage: hedit <pattern>"

def main():     
    if not len(argv) == 2:
        print(_HELP)
        exit(-1)
    os.system(f"sed -i '/{argv[1]}/d' {HISTORY_FILE}") 


if __name__ == "__main__":
    main()
