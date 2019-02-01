import unittest
import bears

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        #spec test case
        self.assertTrue(bears.bears(250))

    def test_bear_02(self):
        #if n==42
        self.assertTrue(bears.bears(42))

    def test_bear_03(self):
        #n is not divisible by 2, 3 or 4, or 5
        self.assertFalse(bears.bears(53))
        self.assertFalse(bears.bears(43))

    def test_bear_04(self):
        #n<42 so False right away
        self.assertFalse(bears.bears(41))

    def test_bear_05(self):
        #if n is a large number
        self.assertTrue(bears.bears(16000))

    def test_bear_06(self):
        # if n==0
        self.assertFalse(bears.bears(0))

    def test_bear_07(self):
        #n is divisible by 2, 3 or 4, and 5
        self.assertFalse(bears.bears(240))
        #n is divisible by 3 and last 2 digits multiplied=0
        self.assertFalse(bears.bears(120))

if __name__ == "__main__":
    unittest.main()
