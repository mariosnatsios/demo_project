import unittest
import time
import api_calls

class TestApi(unittest.TestCase):
    
    REPO_NAME = "NatsRepo" + str(int(time.time()))
    
    def test_1_create_repo(self):
       """
        Create a new GitHub repository.
       """
       api_calls.create_github_repo(self.REPO_NAME)
       
    def test_2_get_repo(self):
        """
            Gets the newly created GitHub repository.
        """
        api_calls.get_github_repo(self.REPO_NAME)
        
    def test_3_create_issue_in_repo(self):
        """
            Creates an issue in the repo.
        """
        api_calls.create_issue_in_repo(self.REPO_NAME)
        
    def test_4_get_issue_in_repo(self):
        """
            Gets the newly created issue.
        """
        api_calls.get_issue_of_repo(self.REPO_NAME)
        
    def test_5_delete_repo(self):
        """
            Deletes the previously created repo.
        """
        api_calls.delete_github_repo(self.REPO_NAME)
        
    def test_6_get_deleted_repo(self):
        """
            Tries to fetch the deleted repo and validates its successfull deletion.
        """
        api_calls.get_deleted_repo(self.REPO_NAME)


if __name__ == '__main__':
    unittest.main()