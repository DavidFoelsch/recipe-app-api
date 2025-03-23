"""
Sample tests
"""

from django.tests import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(selfs):
        """Test adding numbers together"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtract_numbers(selfs):
        """Test subract numbers"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)