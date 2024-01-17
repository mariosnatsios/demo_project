import actions

class HomePage(actions.Actions):
    
    # ----------------------- HELPERS -----------------------
 
    
    # ----------------------- CLICK ------------------------
    def validate_a_side_panel_nav_option(self, option):
        """
            Validate an option in the navigation panel
        """
        path = "//div[contains(@id,'MainMenu')]//div[@id='userRolesMenu']/ul//li" \
               "//a[contains(.,'" + str(option) + "')]"
        self.exists(path)

    
    # ----------------------- CLICK ------------------------
    def click_i_logout_icon(self):
        """
            Clicks the Logout icon
        """
        path = "//div[contains(@class,'profileIcon')]//a[contains(@title,'Logout')]//i"
        self.find_and_click(path)
        
    def click_button_accept_logout(self):
        """
            Accept Logout
        """
        path = "//div[contains(@id, 'LogOutModal')]//div[contains(@class, 'modal-content')]//button[contains(.,'Logout')]"
        self.find_and_click(path)
        
    def click_button_cancel_logout(self):
        """
            Cancel Logout
        """
        path = "//div[contains(@id, 'LogOutModal')]//div[contains(@class, 'modal-content')]//button[contains(.,'Return')]"
        self.find_and_click(path)
        
    
  
   