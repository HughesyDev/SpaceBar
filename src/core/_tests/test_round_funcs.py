import unittest
from unittest.mock import patch
#from unittest.mock import Mock
from src. import add_to_list

class Test_Add_To_List(unittest.TestCase):
    #@patch("src.app.add_to_list")
    def test_add_to_people_list_success(self):
        # Arrange
        people = []
        target = people
        person = "Test User Jr"

        # Act
        add_to_list(target, person)
        expected = "Test User Jr" in people # should return True
        actual = person in people # should return True

        # Assert
        self.assertEqual(expected, actual)

self.bill_payer = bill_payer
        self.orders = {}
        self.roundnum = f"{Round.number_of_rounds}"
        self.number_of_rounds += 1
        print(f"Round number: {self.roundnum}. Bill-payer: {self.bill_payer}")