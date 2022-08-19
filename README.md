# CreateRepo
This is a python script that does the basic house-keeping work of setting up version control.

## Description
The script does the following things:
1. Initialize a remote repository on GitHub
2. Initialize a local repository in the current working directory
3. Link the remote repository with the local repository
4. Add a README.md file in the current working directory
5. Commit all the files in the current working directory and push them to the remote repository

## Dependecies
The script requires Python 3 to run.

## Setting up

1. Get your personal access token from GitHub. Make sure to select **repo** scope for the token. You may find this helpful: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

2. Copy and save your personal access token in a json file like below:
```
    {"GitHubAccessToken" : "paste your token here"}
```
You may want to restrict access to the file to yourself because a personal access token is like your password.

3. Open the `create-repo.py` file and set the values of following variables in `main()` method:
    * `config_file_path` : set it to the path on which your access token json file is.
    * `github_access_token_key`: set it to the name of the key you have used to store access token. If you have used the template shown in previous step, no need to change this variable.

4. Save the `create-repo.py` file.

## Using the script

1. Open `Command Prompt` and go to the folder in which you want to initialize a git repository

2. Run the following command giving a name for your new repository as a command line argument:
```
    python path/to/this/script/create-repo.py new-repository-name
```


