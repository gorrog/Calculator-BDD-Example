from django.test import TestCase
from morelia import run

class ArithmeticTestCase(TestCase):

    def test_basic_arithmetic(self):
        """Run tests for the requirements in calculator.feature """
        run('arithmetic/features/arithmetic.feature', self, verbose=True)
