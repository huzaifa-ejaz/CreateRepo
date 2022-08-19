#import required packages
import sys
import requests
import os
import json

def initializeRemoteRepository(github_repo_API_URL, github_access_token, repo_name):
    #Create the HTTP request with API, Access Token, name of new repository
    head = {"Accept" : "application/vnd.github+json", 
            "Authorization": "token {}".format(github_access_token)}
    data = {"name" : repo_name}
    r = requests.post(github_repo_API_URL, json = data, headers = head)
    
    #Check if the HTTP request is successful
    if r.status_code != 201:
        #If it is unsuccessful, print the error message and end execution
        print(r.json().get("message"))
        print(f"ERROR: The HTTP request failed with status code {r.status_code}")
        sys.exit(1)
    #Else get the URL of the newly created repository and continue
    else:
        remote_url = r.json().get("clone_url")
        print("Remote Repository URL:", remote_url)
        return remote_url

def getGitHubAccessToken(config_file_path, github_access_token_key):
    with open(config_file_path, 'r') as f:
        accessTokens = json.load(f)

    #Get the access token for GitHub API
    access_token = accessTokens[github_access_token_key]

    if(not access_token):
        print("ERROR: GitHub Access Token not found.")
        sys.exit(1)
    else:
        return access_token

def main():

    #Get the name of the new repository from command-line args
    if len(sys.argv) != 2:
        print("ERROR: Repository name not given")
        sys.exit(1)
    else:
        repo_name = sys.argv[1]
        print(repo_name)

    #GitHub API URL to initialize remote repository
    github_repo_API_URL = "https://api.github.com/user/repos"
    
    #GitHub Access Token
    #Note: Save the token in a config json file in the user's home directory. 
    #Your file should look like this:
    #{"GitHubAccessToken" : "ghp_fgdkfh36437GJH"}

    #Path to the configuration file that stores the access token for GitHub API
    config_file_path = r"C:\Users\Syscom\.config\access-tokens.json"

    #Name of the key that has access token as value
    github_access_token_key = "GitHubAccessToken"

    github_access_token = getGitHubAccessToken(config_file_path, github_access_token_key)

    remote_url = initializeRemoteRepository(github_repo_API_URL, github_access_token, repo_name)

    #Initialize a local repository in the current working directory
    os.system("git init")

    #Set the remote on the local repository with name origin and URL from above
    os.system(f"git remote add origin {remote_url}")

    #Add README.md file
    os.system(f"echo # {repo_name} > README.md")

    first_commit_message = "Initial commit"

    #Stage all the files and folders in the current directory
    os.system("git add .")

    #Commit them to the current branch(master) with a suitable commit message
    os.system(f'git commit -m "{first_commit_message}"')
    
    #Push
    #Using the -u tag so that local master branch track origin master branch
    os.system("git push -u origin master")

    print("Repository created.")

if __name__ == "__main__":
    main()
