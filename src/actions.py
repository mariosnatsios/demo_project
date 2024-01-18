from src.conf import CONF
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class Actions():
    """
        Actions class
    """

    def wait_until_element_is_visible(self, target, path_type="xpath"):
        """
            Wait for element to be displayed
        """
        wait = WebDriverWait(CONF.driver, 20)
        
        if path_type == "xpath":
              wait.until(EC.presence_of_all_elements_located((By.XPATH, target)))
              
        if path_type == "css":
              wait.until(EC.presence_of_all_elements_located((By.CSS, target)))
        
        if path_type == "id":
              wait.until(EC.presence_of_all_elements_located((By.ID, target)))
              
        if path_type == "class_name":
              wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, target)))
              
              
    def wait_until_element_is_clickable(self, target, path_type="xpath"):
        """
            Wait for element to be displayed
        """
        wait = WebDriverWait(CONF.driver, 20)
        
        if path_type == "xpath":
            wait.until(EC.element_to_be_clickable((By.XPATH, target)))
            
        if path_type == "css":
            wait.until(EC.element_to_be_clickable((By.CSS, target)))
        
        if path_type == "id":
            wait.until(EC.element_to_be_clickable((By.ID, target)))
            
        if path_type == "class_name":
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, target)))
              
    
    def find_and_click(self, target, path_type="xpath"):
        """
            Waits for element to be visible and then clicks it
        """
        # Wait for element to become visible
        self.wait_until_element_is_visible(target, path_type=path_type)
        self.wait_until_element_is_clickable(target, path_type=path_type)

        success = True
        error_msg = f"{path_type} was NOT FOUND (or is invisible) TO CLICK: {target}"
        
        try:
            if path_type == "xpath":

                CONF.driver.find_element(By.XPATH, target).click()

            if path_type == "css":
                CONF.driver.find_element(By.CSS, target).click()
            
            if path_type == "id":
                CONF.driver.find_element(By.ID, target).click()
                
            if path_type == "class_name":
                CONF.driver.find_element(By.CLASS_NAME, target).click()
                    
        except TimeoutException :
            success = False
        finally:
            assert success == True, error_msg
            
            
            
    def exists(self, target, path_type="xpath"):
        """
            Checks if element exists and is visible
        """
        success = True
        error_msg = f"{path_type} was NOT FOUND OR IS NOT VISIBLE: {target}"
        
        try:
         self.wait_until_element_is_visible(target, path_type=path_type)      
        except TimeoutException :
            success = False
        finally:
            assert success == True, error_msg
            
    
    def not_exists(self, target, path_type="xpath"):
        """
            Checks that element DOES NOT exist in dom (visibel or invisible)
        """
        success = True
        error_msg = f"{path_type} EXISTS IN DOM: {target}"
        
        if path_type == "xpath":
            found_number = len(CONF.driver.find_elements(By.XPATH, target))
            if found_number != 0:
                success = False
                
        if path_type == "css":
            found_number = len(CONF.driver.find_elements(By.CSS, target))
            if found_number != 0:
                success = False
                
        if path_type == "id":
            found_number = len(CONF.driver.find_elements(By.ID, target))
            if found_number != 0:
                success = False
                
        if path_type == "class_name":
            found_number = len(CONF.driver.find_elements(By.CLASS_NAME, target))
            if found_number != 0:
                success = False
                
        assert success == True, error_msg
        
    def existence(self, target, exists=True, path_type="xpath"):
        """
            uses exists or not_exists depending on 'exists'
        """

        if exists:
            self.exists(target, path_type)
        else:
            self.not_exists(target, path_type)
        
        
    def set_text(self, target, text, path_type="xpath", click=False):
        """
            Sets text to element
        """
        
        # Click the input form if neccessary
        if click:
            self.find_and_click(target, path_type=path_type)
        
        if path_type == "xpath":
            # CONF.driver.find_element(By.XPATH, target).clear()
            CONF.driver.find_element(By.XPATH, target).send_keys(text)
    
        if path_type == "css":
            CONF.driver.find_element(By.CSS, target).clear()
            CONF.driver.find_element(By.CSS, target).send_keys(text)
            
        if path_type == "id":
            CONF.driver.find_element(By.ID, target).clear()
            CONF.driver.find_element(By.ID, target).send_keys(text)
                
        if path_type == "class_name":
            CONF.driver.find_element(By.CLASS_NAME, target).clear()
            CONF.driver.find_element(By.CLASS_NAME, target).send_keys(text)

            
    
        
        
        
        
    
            
            
        
            
            