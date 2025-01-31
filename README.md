# GithubAutomationProject

Tool to automate the process of creating a GitHub repository locally and remotely with a one-line command.

## Configuration
```bash
$ python GitAutomation.py --help
```

| Argument  | Description |
| --------  | ----------- | 
| name      | Name of the repository. Required |
| private   | Makes repository private. Optional |

## Requirements
* Python, Git, GitHub Account + GitHub access token
* Create .env file where your GitAutomation.py saved
* Update variables `REPO_PATH`,`GITHUB_URL`, `GITHUB_USER` and `GITHUB_TOKEN` details in the .env file.
* GITHUB_TOKEN="YOUR_GITHUB_TOKEN"
* GITHUB_USER="YOUR_GITIUSERNAME"
* GITHUB_URL="https://github.com/"
* REPO_PATH="LOCAL_REPOPATH"

## Usage

To create a new repo run
```bash
$ pip install -r requirements.txt
$ python GitAutomation.py --name REPOSITORY_NAME
```
