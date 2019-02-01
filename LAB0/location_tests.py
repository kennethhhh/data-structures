import unittest
import location
class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = location.Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_eq(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc2 = location.Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1==loc2, False)
    # Add more tests!
    def test_eq1(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc3 = location.Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1==loc3, True)
    def test_eq2(self):
        loc1 = location.Location("SLO", 35.3, -120.7)
        loc3 = loc1
        self.assertEqual(loc1==loc3, True)


if __name__ == "__main__":
        unittest.main()
