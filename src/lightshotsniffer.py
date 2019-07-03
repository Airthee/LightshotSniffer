# *-* coding: utf8

import sys
import argparse
from tools import Generator
from tools import Downloader
from gui import LssWindow
import tkinter as tk


def main():
    args = parse_arguments()

    # GUI mode
    if args.gui:
        # Lancement de la fenêtre
        root = tk.Tk()
        mainWindow = LssWindow(master=root)
        mainWindow.master.title("LightShotSniffer")
        mainWindow.mainloop()

    # CLI mode
    else:
        # Run sniffer
        startVal = args.start if args.start else "zzzzzz"
        endVal = args.end if args.end else "000000"
        run_sniffer(startVal, endVal)

    return True


def parse_arguments():
    # Parse arguments
    parser = argparse.ArgumentParser()

    # GUI group
    groupGui = parser.add_argument_group("Run with GUI")
    groupGui.add_argument(
        "--gui", help="Run programm with GUI", action="store_true", default=False
    )

    # CLI group
    groupCli = parser.add_argument_group("Run with CLI (default)")
    groupCli.add_argument("--start", help="id to start from", default="zzzzzz")
    groupCli.add_argument("--end", help="id to end to", default="000000")

    return parser.parse_args()


def run_sniffer(start, end):
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


if __name__ == "__main__":
    main()
