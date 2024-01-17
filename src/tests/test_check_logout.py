import sys
sys.path.append('.')
import fixtures
import funcs_login

class Test_Check_Logout(fixtures.Fixtures):
    """
        Checks successful logout after a valid login
    """
    def test_1_check_logout(self):
        """
             Perform valid login then hit the logout button and validate the redirection to the initial login page.
        """
        funcs_login.check_logout()