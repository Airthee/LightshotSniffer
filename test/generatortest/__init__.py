#*-* coding: utf8
import unittest
import sys, os
from generator import Generator

class GeneratorTest(unittest.TestCase):
    def test_next(self):
        self.assertEqual(Generator("000", "ZZZ").next(), "001")
        self.assertEqual(Generator("009", "ZZZ").next(), "00a")
        self.assertEqual(Generator("0A0", "ZZZ").next(), "0a1")
        self.assertEqual(Generator("0AZ", "ZZZ").next(), "0b0")
        self.assertEqual(Generator("0ZZ", "ZZZ").next(), "100")
        self.assertEqual(Generator("ZZY", "ZZZ").next(), "zzz")
        self.assertEqual(Generator("A87", "A87").next(), None)
        self.assertEqual(Generator("111", "000").next(), "110")
        self.assertEqual(Generator("o2xxg0", "000").next(), "o2xxfz")

    def test_previous(self):
        gen = Generator("00z", "zzz")
        self.assertEqual(gen.next(), "010")
        self.assertEqual(gen.next(), "011")
        self.assertEqual(gen.next(), "012")
        self.assertEqual(gen.next(), "013")
        self.assertEqual(gen.previous(), "012")
        self.assertEqual(gen.previous(), "011")
        self.assertEqual(gen.previous(), "010")
        self.assertEqual(gen.previous(), "00z")

if __name__ == "__main__":
    unittest.main()