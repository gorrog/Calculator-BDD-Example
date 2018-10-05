from django.test import TestCase

from morelia import run
from calculator import calculate
import ast

class ArithmeticTestCase(TestCase):

    def test_basic_arithmetic(self):
        """ Run tests for the requirements in calculator.feature """
        run('calculator.feature', self, verbose=True)

    def step_that_we_will_not_use_numbers_greater_that_number_digits(self):
        r'that we will not use numbers greater that 4 digits'
        with self.assertRaises(TypeError):
            calculate(123456, 5, 'add')
        with self.assertRaises(TypeError):
            calculate(1234, 12345, 'add')

    def step_that_we_will_enter_the_input_in_the_order_number1_number2_operator(self):
        r'that we will enter the input in the order number1, number2, operator'
        with self.assertRaises(ValueError):
            calculate('add', 5, 234)
        with self.assertRaises(ValueError):
            calculate(8, 'add', 234)
        with self.assertRaises(ValueError):
            calculate(8, 5, 8)

    def step_we_send_a_request_to_the_calculator(self):
        r'we send a request to the calculator'
        self.result = calculate(1,2,'add')

    def step_the_response_will_start_with_Result(self, Result):
        r'the response will start with "([^"]+)"'
        self.assertIn("Result = ", self.result)

    def step_the_response_will_end_with_a_number(self):
        r'the response will end with a number'
        remainder = self.result.rpartition("Result = ")[2]
        try:
            remainder = ast.literal_eval(remainder)
        except Exception:
            pass
        self.assertTrue(type(remainder) in [int, float])

    def step_we_use_the_add_operator_for_our_operations(self, add):
        r'we use the "([^"]+)" operator for our operations'
        self.operator = 'add'

    def step_our_first_number_is_number1(self, number1):
        r'our first number is (.+)'
        self.number1 = int(number1)

    def step_our_second_number_is_number2(self, number2):
        r'our second number is (.+)'
        self.number2 = int(number2)

    def step_we_call_the_calculator_with_our_numbers_and_operator(self):
        r'we call the calculator with our numbers and operator'
        self.result = calculate(self.number1, self.number2, self.operator)

    def step_the_calculator_will_return_the_value_result(self, result):
        r'the calculator will return the value (.+)'

        remainder = self.result.rpartition("Result = ")[2]
        self.assertEqual(remainder, result)
