import sys
sys.path.append('.')
import fixtures
import funcs_login

class Test_Check_NVG_Login_To_Remind_Username(fixtures.Fixtures):
    """
        Checks navigation from login page to forgot username page
    """
    def test_1(self):
        """
            Navigat to Login Page url: https://ebepirus.natech.gr/en/Account/UserLogin
            Clicks the 'Forgot Username?' link
            Validate page redirection to url: https://ebepirus.natech.gr/en/Account/ForgotUsername
        """
        funcs_login.check_nvg_from_login_to_remind_username()
