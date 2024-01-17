import sys
sys.path.append('.')
import fixtures
import funcs_login


class Test_Valid_Login(fixtures.Fixtures):
    """
        Checks successful login using valid credentilas, for both uppercase and lowercase variations of user
    """
    def test_1_lowercase_username(self):
        """
            Valid login with lowercase username
        """
        funcs_login.perform_valid_login()
        
    def test_2_uppercase_username(self):
        """
            Valid login with lowercase username
        """
        funcs_login.perform_valid_login(upper_username=True)
