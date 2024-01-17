from src.fixtures import Fixtures
from src.funcs_login import check_auto_logout_after_max_connection_time

class Test_Session_Timeout(Fixtures):
    """
        Checks the auto-logout after a timout session
    """
    def test_1(self):
        """
        Logs In
        Wait for 600 secs
        Validate the auto-logout afrer session-timeout by checking the redirection in the Log-In page
        """
        check_auto_logout_after_max_connection_time()