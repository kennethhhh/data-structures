import unittest
import perm_lex

class TestAssign1(unittest.TestCase):
#should return !n permutations, meaning n factorial
# (n)*(n-1)*(n-2)*...*1
# if n=3, 3*2*1==6 permutations

    def test_perm_gen_lex(self):
        #tests simple 2 letter string
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex01(self):
        #tests 3 letter string
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        #same string but different order ---> same permutations but different order
        self.assertEqual(perm_lex.perm_gen_lex('cba'), ['cba', 'cab', 'bca', 'bac', 'acb', 'abc'])

    def test_perm_gen_lex02(self):
        #tests string of length 0
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

    def test_perm_gen_lex03(self):
        #tests string of length 1
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex04(self):
        #tests 4 letter string ---> 4*3*2*1==24 permutations
        self.assertEqual(perm_lex.perm_gen_lex('abcd'),['abcd','abdc','acbd','acdb','adbc','adcb',
                                                        'bacd','badc','bcad','bcda','bdac','bdca',
                                                        'cabd','cadb','cbad','cbda','cdab','cdba',
                                                        'dabc','dacb','dbac','dbca','dcab','dcba'])


if __name__ == "__main__":
        unittest.main()
