import unittest
from unittest.mock import patch
#from unittest.mock import Mock
#from src.app import add_to_list

# Test Response [6] actually throws an error if name is already in faves.
# 
# Need to re-factor that initial, worse re-factor that took input out of a bunch of funcs 
#   (because I didn't know how to handle them at that point and only just remembered about it)


'''
WTF DOES:
 @patch do? 
    - make small test files exploring it
 @patch("builtins")
    - what are they all?
'''



'''class Test_Add_To_List(unittest.TestCase):
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
        self.assertEqual(expected, actual)'''