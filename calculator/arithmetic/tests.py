from django.test import TestCase
from morelia import run

class ArithmeticTestCase(TestCase):

    def test_basic_arithmetic(self):
        """Run tests for the requirements in calculator.feature """
        run('calculator.feature', self, verbose=True)

