#import required packages
import sys
import configparser
import requests
import os
import json

def main():

    #Get the name of the new repository from command-line args
    if len(sys.argv) != 2:
        print("ERROR: Repository name not given")
        sys.exit(1)
    else:
        repo_name = sys.argv[1]
        print(repo_name)

    #Initialize remote repository

    #GitHub API URL to initialize remote repository
    github_repo_API_URL = "https://api.github.com/user/repos"
    
    #GitHub Access Token
    #Note: You should probably save the token in a config json file in the user's home directory. 
    #Note: Preferably, you can restrict permissions on the file to make sure that only that user may 
    #access the config file.

    #TODO: Instead of cfg, read access token from json file
    #Path to the configuration file that stores the access token for GitHub API
    configFilePath = r"C:\Users\Syscom\.config\access-tokens.json"
    gitHubAccessTokenKey = "GitHubAccessToken"

    with open(configFilePath, 'r') as f:
        accessTokens = json.load(f)

    #Get the access token for GitHub API
    accessToken = accessTokens[gitHubAccessTokenKey]

    #Create the HTTP request with API, Access Token, name of new repository
    head = {"Accept" : "application/vnd.github+json", 
            "Authorization": "token {}".format(accessToken)}
    data = {"name" : repo_name}
    r = requests.post(github_repo_API_URL, json = data, headers = head)
    
    #Check if the HTTP request is successful
    if r.status_code != 201:
        #If it is unsuccessful, print the error message and end execution
        print(str(r.content))
        print(f"ERROR: The HTTP request failed with status code {r.status_code}")
        sys.exit(1)
    #Else get the URL of the newly created repository and continue
    else:
        remote_url = r.json().get("clone_url")
        print("Remote Repository URL:", remote_url)

    #Initilize local repository

    is_folder_empty = True
    #Get the current folder we are in
    cwd = os.getcwd()
    #Check if there are files in these folder
    if len(os.listdir(cwd)) > 0 :
        #If so, set the boolean flag
        is_folder_empty = False

    #Initialize a local repository in that folder with the master branch
    os.system("git init")

    #Link the remote to local repository
    
    #Set the remote on the local repository with name origin and URL from above
    os.system(f"git remote add origin {remote_url}")

    #If there are files in the current folder, stage, commit and push them with a suitable message

    #TODO: Create a readme then git add . then commit and push; no need to check whether the folder is empty
    first_commit_message = "Initial commit"
    #If the flag was found to be set.
    if not is_folder_empty:
        #Stage all the files and folders in the current directory
        os.system("git add .")
        #Commit them to the current branch(master) with a suitable commit message
        os.system(f'git commit -m "{first_commit_message}"')
        
        #Push
        #Using the -u tag so that git record that work on local master branch...
        #...needs to pushed to origin master branch
        os.system("git push -u origin master")

    print("Repository created.")

if __name__ == "__main__":
    main()
