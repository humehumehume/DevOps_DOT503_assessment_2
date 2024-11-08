import unittest
from simple_calc import calculator

class testCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()

    def test_add(self):
        try:
            self.assertEqual(self.calc.add(1, 1), 2)  # expected result should be 2
            print("unit test for addition passed")
        except AssertionError:
            print("unit test for addition failed")
            raise

    def test_subtract(self):
        try:
            self.assertEqual(self.calc.subtract(5, 3), 2)  # expected result should be 2
            print("unit test for subtraction passed")
        except AssertionError:
            print("unit test for subtraction failed")
            raise

    def test_percentage(self):
        try:
            self.assertAlmostEqual(self.calc.percentage(50, 200), 25.0)  # expected result should be 25.0
            print("unit test for percentage calculation passed")
        except AssertionError:
            print("unit test for percentage calculation passed")
            raise

    def test_multiply(self):
        try:
            self.assertEqual(self.calc.multiply(3, 4), 12)  # expected result should be 12
            print("unit test for multiplication passed")
        except AssertionError:
            print("unit test for multiplication failed")
            raise

    def test_divide(self):
        try:
            self.assertEqual(self.calc.divide(10, 2), 5)  # expected result should be 5
            print("unit test for division passed")
        except AssertionError:
            print("unit test for division failed")
            raise

        # division by zero test
        try:
            with self.assertRaises(ValueError):
                self.calc.divide(10, 0)
            print("unit test for division by zero test passed")
        except AssertionError:
            print("unit test for division by zero test failed")
            raise

if __name__ == "__main__":
    unittest.main()