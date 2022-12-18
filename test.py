import unittest
from project_rewrite import min_func, max_func, length, multiply, power, div_mod


class TestBasicFunctions(unittest.TestCase):
    def test_min_func(self):
        # Test basic cases
        self.assertEqual(min_func(1, 2), 1)
        self.assertEqual(min_func(-1, 2), -1)
        self.assertEqual(min_func(1, -2), -2)
        self.assertEqual(min_func(-1, -2), -2)
        self.assertEqual(min_func(1, 1), 1)

    def test_max_func(self):
        # Test basic cases
        self.assertEqual(max_func([1, 2, 3, 4]), 4)
        self.assertEqual(max_func([1, 2, 3, 4, -1]), 4)
        self.assertEqual(max_func([1]), 1)
        self.assertEqual(max_func([-1, -2, -3, -4]), -1)

    def test_length(self):
        # Test basic cases
        self.assertEqual(length([1, 2, 3, 4]), 4)
        self.assertEqual(length([]), 0)
        self.assertEqual(length([1]), 1)
        self.assertEqual(length([1, "a", 3]), 3)

    def test_multiply(self):        
        # Test basic cases
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(2, 0), 0)

    def test_power(self):
        # Test basic cases
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 3), 0)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2.5, 3), 15.625)

    def test_div_mod(self):
        self.assertEqual(div_mod(7, 3), (2, 1))
        self.assertEqual(div_mod(0, 3), (0, 0))

    def test_div_mod_positive(self):
        self.assertEqual(div_mod(7, 3), (2, 1))
        self.assertEqual(div_mod(0, 3), (0, 0))


if __name__ == '__main__':
    unittest.main()
