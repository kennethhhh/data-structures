import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        insertion=insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(insertion, 1)
        self.assertEqual(nums, [10, 23])

    def test_bestcase_selection(self):
        nums=[1,2,3,4,5,6,7,8,9,10]
        selection = selection_sort(nums)
        self.assertEqual(selection,45)
        self.assertEqual(nums,[1,2,3,4,5,6,7,8,9,10])

    def test_worstcase_selection(self):
        nums = [10,9,8,7,6,5,4,3,2,1]
        selection=selection_sort(nums)
        self.assertEqual(selection,45)
        self.assertEqual(nums,[1,2,3,4,5,6,7,8,9,10])

    def test_bestcase_insertion(self):
        nums=[1,2,3,4,5,6,7,8,9,10]
        insertion = insertion_sort(nums)
        self.assertEqual(insertion,9)
        self.assertEqual(nums,[1,2,3,4,5,6,7,8,9,10])

    def test_worstcase_insertion(self):
        nums = [10,9,8,7,6,5,4,3,2,1]
        insertion=insertion_sort(nums)
        self.assertEqual(insertion,45)
        self.assertEqual(nums,[1,2,3,4,5,6,7,8,9,10])




if __name__ == '__main__': 
    unittest.main()
