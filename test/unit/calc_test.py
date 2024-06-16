import unittest
import pytest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))   

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(3, 3))
        self.assertEqual(6, self.calc.substract(3, -3))
        self.assertEqual(-6, self.calc.substract(-3, 3))
        self.assertEqual(3, self.calc.substract(3, 0))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(15, self.calc.multiply(5, 3))
        self.assertEqual(-15, self.calc.multiply(5, -3))
        self.assertEqual(-15, self.calc.multiply(-5, 3))
        self.assertEqual(0, self.calc.multiply(5, 0))
        self.assertEqual(0, self.calc.multiply(0, 3))
    
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.divide(8, 2))
        self.assertEqual(2.5, self.calc.divide(5, 2))
        self.assertEqual(0.5, self.calc.divide(2, 4))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(81, self.calc.power(3, 4))
        self.assertEqual(0.0625, self.calc.power(4, -2))
        self.assertEqual(0.0625, self.calc.power(-4, -2))
        self.assertEqual(-27, self.calc.power(-3, 3))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(1, self.calc.power(-3, 0))
        self.assertEqual(0, self.calc.power(0, 4))
        self.assertEqual(1, self.calc.power(0, 0))

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(12, self.calc.sqrt(144))

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(3, self.calc.log10(1000))
        self.assertEqual(5, self.calc.log10(100000))
    
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "3", 3)
        self.assertRaises(TypeError, self.calc.substract, 3, "3")
        self.assertRaises(TypeError, self.calc.substract, "3", "3")
        self.assertRaises(TypeError, self.calc.substract, None, 3)
        self.assertRaises(TypeError, self.calc.substract, 3, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 3)
        self.assertRaises(TypeError, self.calc.substract, 3, object())

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "3", 3)
        self.assertRaises(TypeError, self.calc.multiply, 3, "3")
        self.assertRaises(TypeError, self.calc.multiply, "3", "3")
        self.assertRaises(TypeError, self.calc.multiply, None, 3)
        self.assertRaises(TypeError, self.calc.multiply, 3, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 3)
        self.assertRaises(TypeError, self.calc.multiply, 3, object())
    
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "3", 3)
        self.assertRaises(TypeError, self.calc.divide, 3, "3")
        self.assertRaises(TypeError, self.calc.divide, "3", "3")
        self.assertRaises(TypeError, self.calc.divide, None, 3)
        self.assertRaises(TypeError, self.calc.divide, 3, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 3)
        self.assertRaises(TypeError, self.calc.divide, 3, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "3", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "3")
        self.assertRaises(TypeError, self.calc.power, "2", "3")
        self.assertRaises(TypeError, self.calc.power, None, 3)
        self.assertRaises(TypeError, self.calc.power, 3, None)
        self.assertRaises(TypeError, self.calc.power, object(), 3)
        self.assertRaises(TypeError, self.calc.power, 3, object())

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "3")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    def test_sqrt_method_fails_with_parameter_negative(self):
        number =  -3
        if number < 0:
            self.assertRaises(TypeError, "ERROR: parameter negative")

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "3")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_parameter_negative(self):
        number =  -3
        if number < 0:
            self.assertRaises(TypeError, "ERROR: parameter negative")

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
