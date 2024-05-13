import unittest
from parameterized import parameterized

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    @parameterized.expand([
        (2, 3, 5),
        (-1, 1, 0),
    ])
    def test_add(self, a, b, expected):
        self.assertEqual(add(a, b), expected)

if __name__ == '__main__':
    unittest.main()
