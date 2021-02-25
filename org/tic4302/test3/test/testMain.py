import unittest
import sys
sys.path.append("../../../..")
from org.tic4302.test3.main import get_greeting

#import org.tic4302.test3.main as main_class


class Testing(unittest.TestCase):
    def test_get_greeting(self):
        greeting = get_greeting()
        expected_greeting = 'Hi Aris'
        self.assertEqual(greeting, expected_greeting)

if __name__ == '__main__':
    unittest.main()