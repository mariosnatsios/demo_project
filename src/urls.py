import conf

class Navigate():
    """
        Different page navigations
    """
   
    
    def login_page(self):
        """
            url: https://ebepirus.natech.gr/en/Account/UserLogin
        """
        from pages.login_page import LoginPage
        
        url = "https://ebepirus.natech.gr/en/Account/UserLogin"
        self.wd = conf.CONF.driver
        # Navigate to page
        self.wd.get(url)
        # Return page object
        return LoginPage()
    