import unittest
import time
from src.api_calls import create_github_repo, get_github_repo, create_issue_in_repo, get_issue_of_repo, delete_github_repo, get_deleted_repo

class TestApi(unittest.TestCase):
    
    REPO_NAME = "NatsRepo" + str(int(time.time()))
    
    def test_1_create_repo(self):
       """
        Create a new GitHub repository.
       """
       create_github_repo(self.REPO_NAME)
       
    def test_2_get_repo(self):
        """
            Gets the newly created GitHub repository.
        """
        get_github_repo(self.REPO_NAME)
        
    def test_3_create_issue_in_repo(self):
        """
            Creates an issue in the repo.
        """
        create_issue_in_repo(self.REPO_NAME)
        
    def test_4_get_issue_in_repo(self):
        """
            Gets the newly created issue.
        """
        get_issue_of_repo(self.REPO_NAME)
        
    def test_5_delete_repo(self):
        """
            Deletes the previously created repo.
        """
        delete_github_repo(self.REPO_NAME)
        
    def test_6_get_deleted_repo(self):
        """
            Tries to fetch the deleted repo and validates its successfull deletion.
        """
        get_deleted_repo(self.REPO_NAME)


if __name__ == '__main__':
    unittest.main()