import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simp(self):
        t_list=OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        self.assertEqual(t_list.size(),3)
        self.assertEqual(t_list.remove(2),True)
        self.assertEqual(t_list.size(),2)
        self.assertEqual(t_list.index(3),1)
        t_list.add(4)
        self.assertEqual(t_list.index(3),1)
        self.assertEqual(t_list.python_list(),[1,3,4])

    def test_pythonlist(self):
        t_list=OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(4)
        t_list.remove(1)
        self.assertEqual(t_list.python_list(),[4,5])
        self.assertEqual(t_list.search(1),False)
        self.assertEqual(t_list.python_list_reversed(),[5,4])

    def test_ordered_list(self):
        t_list=OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)
        t_list.add(5)
        self.assertEqual(t_list.index(1),0)
        self.assertEqual(t_list.index(2),1)
        self.assertEqual(t_list.index(3),2)
        self.assertEqual(t_list.index(4),3)
        self.assertEqual(t_list.index(5),4)
        self.assertEqual(t_list.search(5),True)
        self.assertEqual(t_list.search(4),True)
        self.assertEqual(t_list.search(3),True)
        self.assertEqual(t_list.search(2),True)
        self.assertEqual(t_list.search(1),True)
        self.assertEqual(t_list.search(0),False)
        self.assertFalse(t_list.is_empty())

    def test_ordered_list01(self):
        t_list=OrderedList()
        t_list.add(3)
        t_list.add(2)
        t_list.add(1)
        self.assertEqual(t_list.remove(4),False)
        self.assertEqual(t_list.remove(3),True)
        self.assertEqual(t_list.size(),2)
        self.assertEqual(t_list.python_list(),[1,2])
        self.assertEqual(t_list.python_list_reversed(),[2,1])

    def test_ordered_list02(self):
        t_list=OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_ordered_list03(self):
        t_list=OrderedList()
        t_list.add(2040)
        t_list.add(6)
        t_list.add(2)
        t_list.add(7)
        self.assertEqual(t_list.python_list(),[2,6,7,2040])
        self.assertEqual(t_list.pop(2),7)
        with self.assertRaises(IndexError):
            t_list.pop(3)

    def test_ordered_list04(self):
        t_list=OrderedList()
        t_list.add(142)
        t_list.add(14)
        t_list.add(1)
        t_list.add(3)
        self.assertEqual(t_list.index(143), None)
        self.assertEqual(t_list.index(142), 3)
        self.assertEqual(t_list.index(141), None)
        self.assertEqual(t_list.remove(0),False)

    def test_ordered_list05(self):
        t_list=OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        t_list.pop(0)
        t_list.pop(0)
        t_list.pop(0)
        self.assertEqual(t_list.is_empty(),True)
        self.assertEqual(t_list.python_list(),[])
        self.assertEqual(t_list.python_list_reversed(),[])



if __name__ == '__main__': 
    unittest.main()
