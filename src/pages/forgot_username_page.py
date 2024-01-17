import actions

class ForgotUsername(actions.Actions):
    
    # --------------------- VALIDATE -----------------------
    def validate_h5_remind_username(self, exists=True):
        """
            Validates the "Remind Username" header
        """
        path = "//form//h5[contains(., 'Remind Username')]"
        self.existence(path, exists=exists)
        