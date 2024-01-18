from src.conf import CONF
from src.data.login_data import valid_credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By



def login(username, password):
    """
        Navigates to login page and enter credentials in order to login.
    """
    page = CONF.navigate_to.login_page()
    
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
    from src.pages.home import HomePage
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
    from src.pages.login_page import LoginPage
    login_page = LoginPage()
    login_page.validate_p_login_btn(exists=False)
    current_url = CONF.driver.current_url
    assert current_url == "https://ebepirus.natech.gr/en/Home/Index#" + "!", "NOT THE CORRECT LANDING PAGE!!"
    

def check_auto_logout_after_max_connection_time(max_time=600):
    """
        Checks tha an auto-logout occurs after 10 mins(600 secs). After the time period validates the redirection to
        login page.
    """
    success = True
    error_msg = "UNSUCCESSFUL AUTO-LOGOUT AFTER TIME LIMIT!!!"
    # Login
    home_page = perform_valid_login()
    # Validate that the homepage is loaded first
    home_page.validate_a_side_panel_nav_option("Home")
    # Wait for 600ssecs and validate the login page redirection
    from src.pages.login_page import LoginPage
    page = LoginPage()
    try:
        WebDriverWait(CONF.driver, max_time).until(EC.presence_of_all_elements_located((By.XPATH, page.path_form_login_form())))
        print("AUTO-LOGOUT COMPLETD AFTER TIME LIMIT")
    except TimeoutException: 
        success = False
    finally:
         assert success == True, error_msg
                
    
def check_nvg_from_login_to_remind_username():
    """
        Checks navigation from login paage to forgot username page
    """
    page_login = CONF.navigate_to.login_page()
    # Click the 'Forgot Username' link
    page_login.clicks_a_forgot_username()
    # Validate page redirection
    from src.pages.forgot_username_page import ForgotUsername
    new_page = ForgotUsername()
    # Validate header existence in Remind Username form
    new_page.validate_h5_remind_username()
    # Check current url
    current_url = CONF.driver.current_url
    assert current_url=="https://ebepirus.natech.gr/en/Account/ForgotUsername",  "NOT THE CORRECT LANDING PAGE!!"

    
def check_nvg_from_remind_username_to_login():
    """
        Checks navigation from forgot username page to login page
    """ 
    page = CONF.navigate_to.forgot_username_page()
    # Click the 'Return to login page' link
    page.click_a_return_to_login_page()
    # Validate page redirection
    page.validate_h5_remind_username(exists=False)
    from src.pages.login_page import LoginPage
    login_page = LoginPage()
    login_page.validate_p_login_btn()
    current_url = CONF.driver.current_url
    assert current_url == "https://ebepirus.natech.gr/en/Account/UserLogin", "NOT THE CORRECT LANDING PAGE!!"
     
    

    
    
        
   

    
    
    

