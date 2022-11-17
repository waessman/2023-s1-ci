import unittest
from ..math_engine import sum_operation

class MathEngineTestCase(unittest.TestCase):
    def test_add_1_and_2_should_return_3(self):
        # given
        operand_1 = 1
        operand_2 = 2
        expected = 3
        # when
        result = sum_operation(operand_1, operand_2)
        # then
        self.assertEqual(expected, result)

    def test_add_minus_1_and_2_should_return_1(self):
        # given
        operand_1 = -1
        operand_2 = 2
        expected = 1
        # when
        result = sum_operation(operand_1, operand_2)
        # then
        self.assertEqual(expected, result)
