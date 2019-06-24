# *-* coding: utf8
from lightshotsniffer import *
from unittest.mock import patch
import sys


def test_getArgumentValue():
    assert getArgumentValue("--myarg", "defaultVal") == "defaultVal"
    assert getArgumentValue("--myarg2") == None


def test_runSniffer():
    assert runSniffer("o3ka62", "o3ka62") == 0


def test_main():
    testargs = [__file__, "--gui", "False", "--start", "o3ka62", "--end", "o3ka62"]
    with patch.object(sys, "argv", testargs):
        assert main() == True
