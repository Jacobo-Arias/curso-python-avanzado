import unittest
from palindrome import is_palindrome
from primos import is_primo


class Testing(unittest.TestCase):
    def test_palidromes(self):
        self.assertIs(is_palindrome("anitA lava lA tina"), True)
        self.assertEqual(is_palindrome("anitA no lava lA tina"), False)

    def test_primos(self):
        self.assertEqual(is_primo(7), True)
        self.assertEqual(is_primo(18), False)


if __name__ == "__main__":
    unittest.main()
