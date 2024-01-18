import unittest
from src import fixtures
from src.funcs_login import perform_valid_login


class Test_Valid_Login(fixtures.Fixtures):
    """
        Checks successful login using valid credentilas, for both uppercase and lowercase variations of user
    """
    def test_1_lowercase_username(self):
        """
            Valid login with lowercase username
        """
        perform_valid_login()
        
    def test_2_uppercase_username(self):
        """
            Valid login with uppercase username
        """
        perform_valid_login(upper_username=True)

if __name__ == '__main__':
    unittest.main()
