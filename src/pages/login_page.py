import actions


class LoginPage(actions.Actions):   
    
    # ----------------------- HELPERS ------------------------
    def path_input_username_field(self):
        """
            Returns path of username input field
        """
        path = "//input[@id='UserName']"
        return path
    
    def path_input_password_field(self):
        """
            Returns path of password input field
        """
        path = "//input[@id='Password']"
        return path
    
    def path_form_login_form(self):
        """
        Returns path of login form
        """
        path = "//form[@id='LoginForm']"
        return path
    
    # ------------------ CLICK ------------------------
    def click_button_login(self):
        """
            Clicks the LOGIN button
        """
        path = "//button[contains(@class,'login')]"
        self.find_and_click(path)
        
    # ------------------ VALIDATE ------------------------
    def validate_p_login_btn(self, exists=True):
        """
            Validate the existence of login button
        """
        path = "//button[contains(@class,'login')]"
        self.existence(path, exists=exists)
    
    def validate_p_invalid_login_attempt_message(self, error_msg):
        """
            Validates the 'Invalid login attempt.' error message
        """
        path = self.path_form_login_form() + "//p[contains(.,'" + str(error_msg) + "')]"
        self.existence(path)
        
    def validate_p_username_required_message(self):
        """
            Validates the 'The username field is required.' error message
        """
        error_msg = "The username field is required."
        path = self.path_form_login_form() + "//p[contains(.,'" + str(error_msg) + "')]"
        self.existence(path)
    
    def validate_p_password_required_message(self):
        """
            Validates the 'The username field is required.' error message
        """
        error_msg = "The password field is required."
        path = self.path_form_login_form() + "//p[contains(.,'" + str(error_msg) + "')]"
        self.existence(path)

    # ----------------------- SET TEXT ------------------------
    def set_input_username(self, text):
        """
            Sets text in username input field
        """
        path = self.path_input_username_field()
        self.set_text(path, text=text)
        
    def set_input_password(self, text):
        """
            Sets text in password input field
        """
        path = self.path_input_password_field()
        self.set_text(path, text=text)
    