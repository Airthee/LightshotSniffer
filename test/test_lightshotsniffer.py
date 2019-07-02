# *-* coding: utf8
from lightshotsniffer import *
from unittest.mock import patch
import sys

def test_run_sniffer():
    assert run_sniffer("o3ka62", "o3ka62") == 0

def test_main():
    testargs = [__file__, "--start", "o3ka62", "--end", "o3ka62"]
    with patch.object(sys, "argv", testargs):
        assert main() == True
