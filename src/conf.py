
from selenium import webdriver
from selenium.webdriver import ChromeOptions

class ConfigurationHelper():

    driver = None
    navigate_to = None
    
    def set_driver(self, wd):
        self.driver = wd

    def set_browser(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=chrome_options)
        
        return driver
    
    def set_navigate_to(self, nav_obj):
        """
            Loads Navigate() object to naviga_to variable
        """
        self.navigate_to = nav_obj

CONF = ConfigurationHelper()