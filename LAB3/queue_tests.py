import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('thing')
        self.assertEqual(q.dequeue(),'thing')
        self.assertEqual(q.size(),0)

    def test_queue01(self):
        q=Queue(10)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),3)
        self.assertEqual(q.dequeue(),1)

    def test_queue02(self):
        q=Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 5)

    def test_queue03(self):
        q=Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())

    def test_queue04(self):
        q=Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(),1)
        q.enqueue(4)
        with self.assertRaises(IndexError):
            q.enqueue(5)

    def test_queue05(self):
        q=Queue(5)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue06(self):
        q=Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.dequeue()
        q.enqueue(6)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)

    def test_queue07(self):
        q=Queue(6)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        self.assertEqual(q.dequeue(),1)
        self.assertEqual(q.dequeue(),2)
        self.assertEqual(q.dequeue(),3)
        self.assertEqual(q.dequeue(),4)
        self.assertEqual(q.dequeue(),5)
        self.assertEqual(q.dequeue(),6)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),0)

    def test_queue08(self):
        q=Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(),3)




if __name__ == '__main__': 
    unittest.main()
