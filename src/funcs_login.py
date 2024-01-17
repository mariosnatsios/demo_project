import fixtures
import time
import json
from conf import CONF
from data.login_data import valid_credentials



def login(username, password):
    """
        Navigates to login page and enter credentials in order to login.
    """
    page = fixtures.navigate_to.login_page()
    
    page.set_input_username(username)
    page.set_input_password(password)
    page.click_button_login()
    
    return page
    
    

def perform_valid_login(upper_username=False):
    """
        Uses correct username and password to check a valid login
    """
    credentials = valid_credentials()
    if upper_username:
        login(username=credentials["username"].upper(), password=credentials["password"])
    else:
        login(username=credentials["username"], password=credentials["password"])
    
    # Laod new page objecy and validate url after redirection and nav option in the homepage
    from pages.home import HomePage
    home_page = HomePage()
    # Validate navigation option
    home_page.validate_a_side_panel_nav_option("Home")
    # Validate current url
    current_url = CONF.driver.current_url
    assert current_url == "https://ebepirus.natech.gr/en/Home/Index#" + "!", "NOT THE CORRECT LANDING PAGE!!"
    
    return home_page
    

def check_invalid_login(wrong_username=None, wrong_password=None):
    """
        Check invalid login
    """
    # Load the valid credentials
    credentials = valid_credentials()
    if wrong_username:
        page = login(username=wrong_username, password=credentials["password"])
        # Validate error message displayed
        page.validate_p_invalid_login_attempt_message(error_msg="Invalid login attempt.")
    elif wrong_password:
        page =login(username=credentials["username"], password=wrong_password)
        # Validate error message displayed
        page.validate_p_invalid_login_attempt_message(error_msg="Invalid login attempt.")
    else:
        page = login(username="", password="")
        # In case of empty fields both username and password requirement error message is checked.
        page.validate_p_username_required_message()
        page.validate_p_password_required_message()
        
        
def check_logout():
    """
        Perform valid login then hit the logout button and validate the redirection to the initial login page.
    """
    # Perform valid login
    page = perform_valid_login()
    # Hit the Logout button
    page.click_i_logout_icon()
    # Accept Logout from emerged modal
    page.click_button_accept_logout()
    # Validate redirection to login page
    from pages.login_page import LoginPage
    login_page = LoginPage()
    login_page.validate_p_login_btn()
    current_url = CONF.driver.current_url
    assert current_url == "https://ebepirus.natech.gr/en/Account/UserLogin", "NOT THE CORRECT LANDING PAGE!!"
    
def check_cancel_logout():
    """
        Perform valid login then hit the logout button
        Hit the return button from the modal to cancel the logout process
        and validate thet no redirection to the initial login page has occurred.
    """
     # Perform valid login
    page = perform_valid_login()
    # Hit the Logout button
    page.click_i_logout_icon()
    # Cancel Logout from emerged modal
    page.click_button_cancel_logout()
    # Validate no redirection to login page
    page.validate_a_side_panel_nav_option("Home")
    from pages.login_page import LoginPage
    login_page = LoginPage()
    login_page.validate_p_login_btn(exists=False)
    current_url = CONF.driver.current_url
    assert current_url == "https://ebepirus.natech.gr/en/Home/Index#" + "!", "NOT THE CORRECT LANDING PAGE!!"

    
    

    
    
        
   

    
    
    

