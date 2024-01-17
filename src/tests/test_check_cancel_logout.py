from src import fixtures
from src.funcs_login import check_cancel_logout

class Test_Check_Cancel_Logout(fixtures.Fixtures):
    """
        Checks logout canceling after a valid login
    """
    def test_1_check_cancellogout(self):
        """
             Perform valid login then hit the logout button and then the Return button to cancel.
             validate thet no redirection to the initial login page has occurred.
        """
        check_cancel_logout()