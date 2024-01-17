
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

class ConfigurationHelper():

    driver = None
    
    def set_driver(self, wd):
        self.driver = wd

    def set_browser(self):
        service = Service()
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        return driver

CONF = ConfigurationHelper()