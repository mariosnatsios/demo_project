import actions

class ForgotUsername(actions.Actions):
    
    # --------------------- VALIDATE -----------------------
    def validate_h5_remind_username(self, exists=True):
        """
            Validates the "Remind Username" header
        """
        path = "//form//h5[contains(., 'Remind Username')]"
        self.existence(path, exists=exists)
        
    # --------------------- CLICK -----------------------
    def click_a_return_to_login_page(self):
        """
            Clicks the 'Return to login page' link 
        """
        path = "//form//a[contains(@class,'link-muted')]"
        self.find_and_click(path)

        