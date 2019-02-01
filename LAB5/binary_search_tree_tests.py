import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        bst.insert(6, 'other')
        bst.insert(8, 'other')
        bst.insert(7, 'other')
        bst.insert(12, 'other')
        self.assertEqual(bst.find_max(), (12, 'other'))
        self.assertEqual(bst.find_min(), (6, 'other'))
        self.assertEqual(bst.tree_height(), 3)
        self.assertEqual(bst.inorder_list(), [6,7,8,10,12])
        self.assertEqual(bst.preorder_list(), [10,6,8,7,12])
        self.assertTrue(bst.delete(6))
        self.assertEqual(bst.tree_height(), 2)

    def test_bst01(self):
        bst=BinarySearchTree()
        bst.insert(10, "hi")
        bst.insert(6, "hi")
        bst.insert(3, "hi")
        bst.insert(7, "hi")
        bst.insert(12, "hi")
        bst.insert(11, "hi")
        bst.insert(15, "hi")
        bst.insert(16, "hi")
        self.assertEqual(bst.find_max(), (16,"hi"))
        self.assertEqual(bst.find_min(), (3,"hi"))
        bst.insert(3, "wasd")
        self.assertEqual(bst.find_min(), (3, "wasd"))
        self.assertEqual(bst.tree_height(),3)
        self.assertEqual(bst.inorder_list(), [3,6,7,10,11,12,15,16])
        self.assertEqual(bst.preorder_list(), [10,6,3,7,12,11,15,16])
        self.assertTrue(bst.delete(3))
        self.assertEqual(bst.inorder_list(), [6,7,10,11,12,15,16])
        self.assertFalse(bst.delete(3))
        self.assertTrue(bst.delete(7))

    def test_delete1(self):
        bst=BinarySearchTree()
        bst.insert(10, "hi")
        bst.insert(8, "hi")
        bst.insert(5, "hi")
        bst.insert(20, "hi")
        bst.insert(15, "hi")
        bst.insert(3, "hi")
        bst.insert(6, "hi")
        self.assertFalse(bst.delete(7))
        self.assertTrue(bst.delete(3))
        self.assertEqual(bst.inorder_list(),[5,6,8,10,15,20])
        self.assertEqual(bst.preorder_list(),[10,8,5,6,20,15])
        self.assertTrue(bst.delete(8))
        self.assertEqual(bst.inorder_list(), [5, 6, 10, 15, 20])

    def test_delete2(self):
        bst=BinarySearchTree()
        self.assertFalse(bst.search(10))
        self.assertFalse(bst.find_min())
        self.assertFalse(bst.find_max())
        self.assertEqual(bst.tree_height(),None)
        self.assertFalse(bst.delete(1))
        bst.insert(10,"hi")
        bst.insert(5,"hi")
        bst.insert(20,"hi")
        bst.insert(3,"hi")
        bst.insert(8,"hi")
        bst.insert(9,"hi")
        bst.insert(6,"hi")
        bst.insert(15,"hi")
        bst.insert(40,"hi")
        bst.insert(50,"hi")
        bst.insert(30,"hi")
        self.assertTrue(bst.delete(5))
        self.assertTrue(bst.delete(20))
        print(bst.root.right.right.left)
        self.assertEqual(bst.inorder_list(),[3,6,8,9,10,15,30,40,50])

    def test_bst(self):
        bst=BinarySearchTree()
        bst.insert(10, "yolo")
        self.assertEqual(bst.root.get_data(),"yolo")
        self.assertEqual(bst.root.get_key(),10)

    def test_bst1(self):
        bst=BinarySearchTree()
        bst.insert(10,"fml")
        self.assertTrue(bst.delete(10))

    def test_bst2(self):
        bst=BinarySearchTree()
        bst.insert(10,"fml")
        bst.insert(5,"fml")
        bst.insert(30,"fml")
        bst.insert(40,"fml")
        bst.insert(35,"fml")
        bst.insert(50,"fml")
        self.assertTrue(bst.delete(30))
        self.assertTrue(bst.delete(50))
        self.assertTrue(bst.delete(35))

    def test_bst3(self):
        bst=BinarySearchTree()
        bst.insert(10, "pls")
        bst.insert(5, "pls")
        bst.insert(20, "pls")
        bst.insert(30, "pls")
        bst.insert(40, "pls")
        bst.insert(50, "pls")
        bst.insert(49, "pls")
        bst.insert(48, "pls")
        self.assertTrue(bst.delete(40))
        self.assertTrue(bst.delete(50))

    def test_bst4(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(40)
        bst.insert(50)
        self.assertTrue(bst.delete(30))

    def test_bst5(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        self.assertTrue(bst.delete(30))

    def test_bst6(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        bst.insert(40)
        bst.insert(50)
        self.assertTrue(bst.delete(30))

    def test_bst7(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        bst.insert(40)
        bst.insert(50)
        bst.insert(35)
        self.assertTrue(bst.delete(30))

    def test_bst8(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        bst.insert(25)
        bst.insert(27)
        bst.insert(28)
        self.assertTrue(bst.delete(20))
        self.assertEqual(bst.inorder_list(),[10,25,27,28,30])

    def test_bst9(self):
        bst=BinarySearchTree()
        bst.insert(30)
        bst.insert(40)
        bst.insert(35)
        bst.insert(50)
        bst.insert(60)
        bst.insert(55)
        bst.insert(70)
        self.assertTrue(bst.delete(40))
        self.assertEqual(bst.inorder_list(),[30,35,50,55,60,70])

if __name__ == '__main__': 
    unittest.main()