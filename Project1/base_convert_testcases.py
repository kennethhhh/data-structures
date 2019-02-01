import unittest
import base_convert

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(base_convert.convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(base_convert.convert(30,4),"132")

    def test_base16(self):
        #test for hexadecimal
        self.assertEqual(base_convert.convert(316,16),"13C")

    def test_base_convert01(self):
        #test for converting number to same base, should always return 10
        self.assertEqual(base_convert.convert(4,4),"10")
        self.assertEqual(base_convert.convert(2,2),"10")
        self.assertEqual(base_convert.convert(16,16),"10")

    def test_base_convert02(self):
        #test for every hexadecimal
        self.assertEqual(base_convert.convert(314,16),"13A")
        self.assertEqual(base_convert.convert(315,16),"13B")
        self.assertEqual(base_convert.convert(316,16),"13C")
        self.assertEqual(base_convert.convert(317,16),"13D")
        self.assertEqual(base_convert.convert(318,16),"13E")
        self.assertEqual(base_convert.convert(319,16),"13F")

    def test_base_convert03(self):
        #test if base is > number, should return the number back
        self.assertEqual(base_convert.convert(9,11),"9")

if __name__ == "__main__":
        unittest.main()