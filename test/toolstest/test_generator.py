#*-* coding: utf8
from tools import Generator

class GeneratorTest():
  def test_next(self):
      assert Generator("000", "ZZZ").next() == "001"
      assert Generator("009", "ZZZ").next() == "00a"
      assert Generator("0A0", "ZZZ").next() == "0a1"
      assert Generator("0AZ", "ZZZ").next() == "0b0"
      assert Generator("0ZZ", "ZZZ").next() == "100"
      assert Generator("ZZY", "ZZZ").next() == "zzz"
      assert Generator("A87", "A87").next() == None
      assert Generator("111", "000").next() == "110"
      assert Generator("o2xxg0", "000").next() == "o2xxfz"

  def test_previous(self):
      gen = Generator("00z", "zzz")
      assert gen.next() == "010"
      assert gen.next() == "011"
      assert gen.next() == "012"
      assert gen.next() == "013"
      assert gen.previous() == "012"
      assert gen.previous() == "011"
      assert gen.previous() == "010"
      assert gen.previous() == "00z"