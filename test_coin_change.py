import unittest
from coin_change import getWays

class TestChange(unittest.TestCase):
    
    def test_simple_1(self):
        first_multiple_input = '''
        4 3
        1 2 3
        '''
        n, _, *c = map(int,first_multiple_input.split())
        result = getWays(n, c)
        self.assertEqual(result, 4)

    def test_simple_2(self):
        first_multiple_input = '''
        10 4
        2 5 3 6
        '''
        n, _, *c = map(int,first_multiple_input.split())
        result = getWays(n, c)
        self.assertEqual(result, 5)

    
