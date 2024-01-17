from src import fixtures
from src.funcs_login import check_nvg_from_remind_username_to_login


class Test_Check_NVG_Remind_Username_To_Login(fixtures.Fixtures):
    """
        Checks from login page to forgot username page
    """
    def test_1(self):
        """
            Navigate to Remind Username page url: https://ebepirus.natech.gr/en/Account/ForgotUsername
            Click the 'Return to login page' link
             Validate page redirection to url: https://ebepirus.natech.gr/en/Account/UserLogin
        """
        check_nvg_from_remind_username_to_login()
