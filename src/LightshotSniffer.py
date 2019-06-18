#*-* coding: utf8

import sys
from tools import Generator
from tools import Downloader

def main():
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"

    # Get arguments values
    startVal = getArgumentValue("--start", "zzzzzz")
    endVal = getArgumentValue("--end", "000000")

    # For each value
    # Get url and ask to keep or not the image
    gen = Generator(startVal, endVal)
    while True:
        value = gen.value()
        img = Downloader.downloadById(value)
        # if img:
        #     pass

        # If we finished, break the loop
        if not gen.next():
            break

def getArgumentValue(argName, defaultValue = None):
    try:
        argIndex = sys.argv.index(argName)
        return sys.argv[argIndex + 1]
    except ValueError:
        return

if __name__ == "__main__":
    main()