import unittest
from unittest.mock import patch
#from unittest.mock import Mock
from src.app import add_to_list



'''
WTF DOES:
 @patch do? 
    - make small test files exploring it
 @patch("builtins")
    - what are they all?
'''



class Test_Add_To_List(unittest.TestCase):
    @patch("src.app.add_to_list")
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


'''class Test_Response_Func_Returns_Valid(unittest.TestCase):
    #@patch("")
    def test_response(self, mock_answer):
        pass'''

# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()

# .side_effect
# .return_value
# .assertcalled once with
# @patch("src.table.print_divider")
# @patch("bultins.print")