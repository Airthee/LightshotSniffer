#*-* coding: utf8
from lightshotsniffer import *

def test_getArgumentValue():
    assert getArgumentValue("--myarg", "defaultVal") == "defaultVal"
    assert getArgumentValue("--myarg2") == None

def test_runSniffer():
    assert runSniffer('o3ka62', 'o3ka62') == 0