import unittest
from unittest.mock import Mock
from unittest.mock import patch

# Will use this area to learn testing to a better degree. With self-contained functions / classes to test in isolation.
# Then apply that to my main app funcs/classes.

drinks = []

def add_to_drink_with_args(drink):
    global drinks
    drinks.append(drink)
    pass

add_to_drink_with_args("Coke")
print(drinks)

#adder(10, 12)

class test_(unittest.TestCase):
    # @patch
    def test_printer(self):
        pass

        # Arrange
        # Act
        # Assert


