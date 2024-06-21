import unittest

from unittest.mock import patch
from exam.main import MeatPerson


class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='Sample')
    def test_greet_with_mocked_input(self, mock_input):
        expected_output = "Hello Boss, Sample!"
        meat_person = MeatPerson()
        output = meat_person.main()
        self.assertEqual(output, expected_output)


#
# if __name__ == '__main__':
#     unittest.main()
