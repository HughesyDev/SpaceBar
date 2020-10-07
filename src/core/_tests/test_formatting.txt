import unittest
from unittest.mock import patch
#from unittest.mock import Mock
from src.core.formatting.formatting_funcs import print_line

class Test_Formatting(unittest.TestCase):
    @patch("src.core.formatting.formatting_funcs.print_line")
    @patch("builtins.print")
    def test_print_line_returns_valid_width(self, print_mock, print_line_mock):
        # ARRANGE
        TEST_WIDTH = 20
        EXPECTED = print_mock(f"+" + "=" * 20 + "+")

        # ACT
        ACTUAL   = print_line_mock(TEST_WIDTH)
        
        # ASSERT
        return self.assertTrue(ACTUAL, EXPECTED)