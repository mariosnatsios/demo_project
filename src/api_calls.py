import requests, json
from src.data.api_data import github_user_info


def create_github_repo(repo_name):
    """
        Creates a Github repo
    """
    url = "https://api.github.com/user/repos"
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    
    data = json.dumps(
        {
            "name": str(repo_name),
            "description": "Nats made this repo!"
        }
    )
    
    response = requests.post(url=url, data=data, headers=headers)
    # Check response
    assert response.status_code == 201,  f"Failed to create repository. Status: {response.status_code}"
    
    print(response)
    return response
    
    
def get_github_repo(repo_name):
    """
        Creates a Github repo
    """
    username = github_user_info["username"]
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    
    
    response = requests.get(url=url, headers=headers)
    # Check response
    assert response.status_code == 200,  f"Failed to get repository. Status: {response.status_code}"
    
    print(response)
    return response

def create_issue_in_repo(repo_name):
    """
        Creates a Github repo
    """
    username = github_user_info["username"]
    url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    
    data = json.dumps(
        {
            "title": "Found a bug",
            "body": "I am having a problem with this."
        }
    )
    
    response = requests.post(url=url, data=data, headers=headers)
    # Check response
    assert response.status_code == 201,  f"Failed to create an issue in repository. Status: {response.status_code}"
    return response

def get_issue_of_repo(repo_name, issue_number=1):
    """
        Gets repository issue 
    """
    username = github_user_info["username"]
    url = f"https://api.github.com/repos/{username}/{repo_name}/issues/{issue_number}"
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    
    
    response = requests.get(url=url, headers=headers)
    # Check response
    assert response.status_code == 200,  f"Failed to retrieve issue. Status: {response.status_code}"    
    return response

def delete_github_repo(repo_name):
    """
        Deletes GitHub repo..
    """
    username = github_user_info["username"]
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    url = f" https://api.github.com/repos/{username}/{repo_name}"
    
    response = requests.delete(url=url, headers=headers)
    # Check response
    assert response.status_code == 204,  f"Failed to delete repository. Status: {response.status_code}"
    print(response)
    
    
def get_deleted_repo(repo_name):
    """
        Validates the repo deletion by trying to fetch it
    """
    username = github_user_info["username"]
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    token = github_user_info["api_token"]
    headers = {"Authorization": "Bearer " + str(token)}
    
    
    response = requests.get(url=url, headers=headers)
    # Check response
    assert response.status_code == 404,  f"Repository still exists. Status: {response.status_code}"
    

    