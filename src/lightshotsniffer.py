# *-* coding: utf8

import sys
from tools import Generator
from tools import Downloader
from gui import LssWindow
import tkinter as tk


def main():
    withGui = getArgumentValue("--gui", "True").upper() in ["TRUE", "YES", "OK", "1"]

    # CLI mode
    if not withGui:
        # Run sniffer
        startVal = getArgumentValue("--start", "zzzzzz")
        endVal = getArgumentValue("--end", "000000")
        runSniffer(startVal, endVal)

    # GUI mode
    else:
        # Lancement de la fenêtre
        root = tk.Tk()
        mainWindow = LssWindow(master=root)
        mainWindow.master.title("LightShotSniffer")
        mainWindow.mainloop()
        print("C'est partit")


def runSniffer(start, end):
    # For each value
    # Get url and ask to keep or not the image
    gen = Generator(start, end)
    while True:
        value = gen.value()
        img = Downloader.get_url_by_id(value)
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
