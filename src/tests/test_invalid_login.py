import sys
import fixtures
import funcs_login
import time



class Test_Invalid_Login(fixtures.Fixtures):
    """
        Checks invalid login scenarios
    """
    WRONG_PASS = f"WrongPass{str(int(time.time()))}"
    WRONG_USERNAME =  f"WrongUsername{str(int(time.time()))}"
    
    def test_1_incorrect_password(self):
        """
            Navigate to the finance application's login page.
            Enter a valid username.
            Enter an incorrect password.
            Click on the login button.
            Verify that an appropriate error message is displayed.
        """
        funcs_login.check_invalid_login(wrong_password=self.WRONG_PASS)
        
    def test_2_incorrect_username(self):
        """
            Navigate to the finance application's login page.
            Enter an invalid username.
            Enter a valid password.
            Click on the login button.
            Verify that an appropriate error message is displayed.
        """
        funcs_login.check_invalid_login(wrong_username=self.WRONG_USERNAME)
    
    def test_3_empty_field(self):
        """
             Submit the login form with empty username and password fields.
             Verify appropriate error messages for both fields.
        """
        funcs_login.check_invalid_login()

