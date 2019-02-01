import unittest
import lab1

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing if list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            lab1.max_list_iter(tlist)

    def test_max_list_iter01(self):
        """ Testing if list is empty"""
        self.assertEqual(lab1.max_list_iter([]),None)

    def test_max_list_iter02(self):
        """Finds max of ordered list"""
        self.assertEqual(lab1.max_list_iter([1,2,3,4]),4)

    def test_max_list_iter03(self):
        """Finds max of unordered list"""
        self.assertEqual(lab1.max_list_iter([5,3,4,2]),5)

    def test_max_list_iter04(self):
        """Finds max of all same numbers"""
        self.assertEqual(lab1.max_list_iter([5,5,5]),5)

    def test_max_list_iter05(self):
        """Finds max of when 2 are max"""
        self.assertEqual(lab1.max_list_iter([5,5,4]),5)

    def test_max_list_iter06(self):
        """Finds max of one number"""
        self.assertEqual(lab1.max_list_iter([5]),5)




    def test_reverse_rec(self):
        """Reverses an ordered list"""
        self.assertEqual(lab1.reverse_rec([1,2,3]),[3,2,1])

    def test_rever_rec01(self):
        """Test for empty list"""
        self.assertEqual(lab1.reverse_rec([]),[])

    def test_rever_rec02(self):
        """Test for if list is None"""
        with self.assertRaises(ValueError):
            lab1.reverse_rec(None)

    def test_rever_rec03(self):
        """Test for unordered list"""
        self.assertEqual(lab1.reverse_rec([1,6,74,3,2,4]),[4,2,3,74,6,1])

    def test_rever_rec04(self):
        """Test for list of 1 number"""
        self.assertEqual(lab1.reverse_rec([1]),[1])

    def test_rever_rec05(self):
        """Test for list of same numbers"""
        self.assertEqual(lab1.reverse_rec([3,3,3]),[3,3,3])




    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(lab1.bin_search(4, low, high, list_val), 4 )

    def test_bin_search01(self):
        """Test for list equal to None"""
        with self.assertRaises(ValueError):
            lab1.bin_search(1,2,3,None)

    def test_bin_search02(self):
        """Test for list equal to None and high<low"""
        with self.assertRaises(ValueError):
            lab1.bin_search(1,4,3,None)

    def test_bin_search03(self):
        """Test for high<low and high is not equal to target"""
        self.assertEqual(lab1.bin_search(1,4,2,[0,1,2,3,4,5]),None)

    def test_bin_search04(self):
        """Test for negative numbers"""
        list_val = [-10,-9,-8,-7,-4,-2,-1,0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(lab1.bin_search(-1,low,high,list_val),6)

    def test_bin_search05(self):
        """Test for target not in list"""
        list_val = [0.1,0.2,0.3,2.2,5.7,6.0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(lab1.bin_search(-1,low,high,list_val),None)

    def test_bin_search06(self):
        """Test for floats"""
        list_val = [0.1,0.2,0.3,2.2,5.7,6.0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(lab1.bin_search(0.1,low,high,list_val),0)

    def test_bin_search07(self):
        """Test for target appears more than once
        Searches for the last one and returns that index"""
        list_val = [0.1,0.1,0.1,2.2,5.7,6.0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(lab1.bin_search(0.1,low,high,list_val),2)

    def test_bin_search08(self):
        """Test for target directly in middle"""
        list_val = [0.1,0.2,0.3,2.2,5.7,6.0,7.0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(lab1.bin_search(2.2,low,high,list_val),3)

    def test_bin_search09(self):
        """Test for looking at 1 index and target not found"""
        list_val = [0.1,0.2,0.3,2.2,5.7,6.0,7.0]
        low = 0
        high = 0
        self.assertEqual(lab1.bin_search(2.2,low,high,list_val),None)

    def test_bin_search10(self):
        """Test for looking at 1 index and target is there"""
        list_val = [0.1,0.2,0.3,2.2,5.7,6.0,7.0]
        low = 0
        high = 0
        self.assertEqual(lab1.bin_search(0.1,low,high,list_val),0)


if __name__ == "__main__":
        unittest.main()

    
