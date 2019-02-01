import unittest
import io, sys
import separator

# Run this unittest file without passing any command-line arguments
# other than ones you want to pass to unittest such as -values

class Test_seperator(unittest.TestCase):

    def setUp(self):
        # Add a spot to argv that we can use to pass command-line 
        # arguments to the main function in the separator module
        sys.argv.append(None)

    def test_01(self):
        sys.argv[1] = 6 # Simulates passing 6 on the command line
        sys.stdout = student_output = io.StringIO()        
        sys.stdin = io.StringIO("1 2 1.2 2.3\n3\n4\n7.8 garbage, 12\n")
        expected_out = "Integers: 1 2 3 4 \nFloats: 1.2 2.3 7.8"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.argv[1] = 4 # Simulates passing 4 on the command line (More than N integers)
        sys.stdout = student_output = io.StringIO()        
        sys.stdin = io.StringIO("1 2 3\n4 5 6\n")
        expected_out = "Integers: 1 2 3 4 \nFloats:"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_03(self):
        sys.argv[1] = 4 # Fewer than 4 integers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2 3\n\n")
        expected_out = "Integers: 1 2 3 \nFloats:"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_04(self):
        sys.argv[1] = 4 # Simulates Exactly 4 integers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2 3\n4\n\n")
        expected_out = "Integers: 1 2 3 4 \nFloats:"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_05(self):
        sys.argv[1] = 4 # Simulates More than 4 non-integer numbers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1 2.2 3.3\n4.4 5.5 6.6\n")
        expected_out = "Integers: \nFloats: 1.1 2.2 3.3 4.4"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_06(self):
        sys.argv[1] = 4 # Simulates Exactly 4 non-integer numbers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1 2.2 3.3\n4.4\n\n")
        expected_out = "Integers: \nFloats: 1.1 2.2 3.3 4.4"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_07(self):
        sys.argv[1] = 4 # Simulates Fewer than 4 non-integer numbers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1 2.2 3.3\n\n")
        expected_out = "Integers: \nFloats: 1.1 2.2 3.3"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_08(self):
        sys.argv[1] = 4 # Simulates More than 4 integers but fewer than 4 non-integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2.2 3\n4 5 6 7\n")
        expected_out = "Integers: 1 3 4 5 \nFloats: 2.2"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_09(self):
        sys.argv[1] = 4 # Simulates More than 4 non-integer numbers but fewer than 4 integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1 2.2 3.3\n4 5.5 6.6\n")
        expected_out = "Integers: 4 \nFloats: 1.1 2.2 3.3 5.5"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_10(self):
        sys.argv[1] = 4 # Simulates Exactly 4 integers and exactly 4 non-integers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1 2.2 3.3\n4.4 5 6 7\n8\n\n")
        expected_out = "Integers: 5 6 7 8 \nFloats: 1.1 2.2 3.3 4.4"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_11(self):
        sys.argv[1] = 4 # Simulates Fewer than 4 integers and fewer than 4 non-integer numbers (followed by a blank line)
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1\n1\n\n")
        expected_out = "Integers: 1 \nFloats: 1.1"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_12(self):
        sys.argv[1] = 4 # First invalid value is preceded by more than 4 integers and fewer than 4 non-integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1\n1 2 3 4\n5 6 h\n")
        expected_out = "Integers: 1 2 3 4 \nFloats: 1.1"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_13(self):
        sys.argv[1] = 4 # First invalid value is preceded by more than 4 non-integers and fewer than 4 integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1\n2 3.3 4.4 5.5 6.6 h\n")
        expected_out = "Integers: 2 \nFloats: 1.1 3.3 4.4 5.5"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_14(self):
        sys.argv[1] = 4 # First invalid value is preceded by exactly 4 integers and exactly 4 non-integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1\n2.2 3.3 4.4\n5 6 7 8\nh\n")
        expected_out = "Integers: 5 6 7 8 \nFloats: 1.1 2.2 3.3 4.4"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_15(self):
        sys.argv[1] = 4 # First invalid value is preceded by fewer than 4 integers and fewer than 4 non-integers
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1.1\n2\nh\n")
        expected_out = "Integers: 2 \nFloats: 1.1"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_16(self):
        sys.argv[1] = 4 # The input contains only invalid values
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("h\n")
        expected_out = "Integers: \nFloats:"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_17(self):
        sys.argv[1] = 4 # The input contains no values at all (blank line right away).
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("\n")
        expected_out = "Integers: \nFloats:"
        separator.main()
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
