# *-* coding: utf8

import sys
from tools import Generator
from tools import Downloader


def main():
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"

    # Get arguments values
    # Run sniffer
    startVal = getArgumentValue("--start", "zzzzzz")
    endVal = getArgumentValue("--end", "000000")
    runSniffer(startVal, endVal)


def runSniffer(start, end):
    # For each value
    # Get url and ask to keep or not the image
    gen = Generator(start, end)
    while True:
        value = gen.value()
        img = Downloader.downloadById(value)
        # if img:
        #     pass

        # If we finished, break the loop
        if not gen.next():
            break
    return 0


def getArgumentValue(argName, defaultValue=None):
    try:
        argIndex = sys.argv.index(argName)
        return sys.argv[argIndex + 1]
    except ValueError:
        return defaultValue


if __name__ == "__main__":
    main()
