import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_stack(self):
        #checking when stack is has no elements in it
        stack = Stack(10)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)

    def test_stack01(self):
        #testing index error for push
        stack= Stack(1)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_stack02(self):
        #testing index error for pop and peek
        stack= Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_stack03(self):
        stack = Stack(10)
        stack.push(1)
        stack.push(2)
        stack.push(30)
        self.assertFalse(stack.is_full())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(),30)
        self.assertEqual(stack.size(),3)
        self.assertEqual(stack.pop(),30)

    def test_stack04(self):
        stack = Stack(10)
        stack.push(1)
        stack.push(2)
        stack.push(30)
        self.assertFalse(stack.is_full())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.peek(),30)
        self.assertEqual(stack.size(),3)
        self.assertEqual(stack.pop(),30)
        self.assertEqual(stack.pop(),2)
        self.assertEqual(stack.pop(),1)
        self.assertTrue(stack.is_empty())

    def test_stack05(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(30)
        self.assertTrue(stack.is_full())



if __name__ == '__main__': 
    unittest.main()
