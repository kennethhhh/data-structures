# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_eval_07(self):
        with self.assertRaises(ValueError):  # used to check for exception
            postfix_eval("2 0 /")

    def test_postfix_eval_00(self):
        self.assertAlmostEqual(postfix_eval("0 2 /"), 0)

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("4 2 ^ 5 - 3 + 7 7 / -"), 13)

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval("2 3 + 2 ^"), 25)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("5 2 /"), 2.5)

    def test_postfix_eval_11(self):
        self.assertEqual(postfix_eval("2 4 -"), -2)

    def test_postfix_eval_12(self):
        self.assertEqual(postfix_eval("2 4 +"), 6)

    def test_postfix_eval_13(self):
        self.assertEqual(postfix_eval("2 3 2 ^ ^"), 512)

    def test_postfix_eval_14(self):
        self.assertEqual(postfix_eval("12"),12)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("5 + 2 * 4 + 7 - 2 + 4 * ( 6 / 2 - 2 ) - 4"), "5 2 4 * + 7 + 2 - 4 6 2 / 2 - * + 4 -")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("5 + 2 * 4 + 7 - 2 + 4 * ( 6 / 2 - 2 ) - 4 ^ 3"),"5 2 4 * + 7 + 2 - 4 6 2 / 2 - * + 4 3 ^ -")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix("3 + 4 + 5 + 6 + 7 + 8"), "3 4 + 5 + 6 + 7 + 8 +")

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("( 5 + ( 2 * ( 4 + ( 7 - ( 2 + ( 4 * ( 6 / 2 - 2 ) ) ) ) ) ) ) - 4 ^ 3"), "5 2 4 7 2 4 6 2 / 2 - * + - + * + 4 3 ^ -")

    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix("5 + 5 * ( 10 / 2 - 3 ) ^ 4 / 2"),"5 5 10 2 / 3 - 4 ^ * 2 / +")

    def test_infix_to_postfix_07(self):
        self.assertEqual(infix_to_postfix("2 + ( 4 ^ 3 ) - 2"), "2 4 3 ^ + 2 -")

    def test_infix_to_postfix_08(self):
        self.assertEqual(infix_to_postfix('2 ^ 4 ^ 3 ^ 7'), "2 4 3 7 ^ ^ ^")

    def test_infix_to_postfix_09(self):
        #really big equation
        self.assertEqual(infix_to_postfix("6 + 6 * 6 + 2 + 7 - 5 - ( 1 * 8 * 6 + 4 * 7 ^ 2 / 9 ^ 1 ^ 2 / 3 ) ^ 3 + 4 ( 8 ^ 6 ) * 7 * 2 - 8 ^ 8 ^ 9 - 7 + 6 + 6 ^ 4 ^ 6 - 4 ( 3 + 6 ) + 3 * 5 / 8 - 2 ^ 9 / 4 ^ 2 * ( 4 * 9 + 3 - 3 / 5 ^ 3 - 1 ) + 2 - 4 ^ 9"), "6 6 6 * + 2 + 7 + 5 - 1 8 * 6 * 4 7 2 ^ * 9 1 2 ^ ^ / 3 / + 3 ^ - 4 8 6 ^ 7 * 2 * + 8 8 9 ^ ^ - 7 - 6 + 6 4 6 ^ ^ + 4 3 6 + - 3 5 * 8 / + 2 9 ^ 4 2 ^ / 4 9 * 3 + 3 5 3 ^ / - 1 - * - 2 + 4 9 ^ -")

    def test_infix_to_postfix_10(self):
        self.assertEqual(infix_to_postfix("2 * 3 + 3"),"2 3 * 3 +")

    def test_infix_to_postfix_11(self):
        self.assertEqual(infix_to_postfix("( 4 + 5 ) * 2 * 4"), "4 5 + 2 * 4 *")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("* - 5 6 7"), "5 6 - 7 *")




if __name__ == "__main__":
    unittest.main()
