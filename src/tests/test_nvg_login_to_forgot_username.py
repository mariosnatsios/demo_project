import sys
sys.path.append('.')
import fixtures
import funcs_login

class Test_Check_Logoutfix(fixtures.Fixtures):
    """
        Checks from login paage to forgot username page
    """
    def test_1(self):
        funcs_login.check_nvg_from_login_to_remind_username()
