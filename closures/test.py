import unittest
from closures4 import make_divider_of


class Testing(unittest.TestCase):
    def test_division(self):
        d_10 = make_divider_of(10)
        self.assertEqual(d_10(100), 10)
        self.assertEqual(d_10(50), 5)


if __name__ == "__main__":
    unittest.main()
