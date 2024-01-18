from src.conf import CONF

class Navigate():
    """
        Different page navigations
    """
   
    
    def login_page(self):
        """
            url: https://ebepirus.natech.gr/en/Account/UserLogin
        """
        from src.pages.login_page import LoginPage
        
        url = "https://ebepirus.natech.gr/en/Account/UserLogin"
        self.wd = CONF.driver
        # Navigate to page
        self.wd.get(url)
        # Return page object
        return LoginPage()
    
    def forgot_username_page(self):
        """
            url:https://ebepirus.natech.gr/en/Account/ForgotUsername
        """
        from src.pages.forgot_username_page import ForgotUsername
        
        url = "https://ebepirus.natech.gr/en/Account/ForgotUsername"
        self.wd = CONF.driver
        # Navigate to page
        self.wd.get(url)
        # Return page object
        return ForgotUsername()
    
    