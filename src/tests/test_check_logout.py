from src import fixtures
from src.funcs_login import check_logout

class Test_Check_Logout(fixtures.Fixtures):
    """
        Checks successful logout after a valid login
    """
    def test_1_check_logout(self):
        """
             Perform valid login then hit the logout button and validate the redirection to the initial login page.
        """
        check_logout()