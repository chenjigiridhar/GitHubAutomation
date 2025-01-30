#!/usr/bin/env python3
import argparse
import os
import requests
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 



parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private



if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

headers = {
    "Authorization": "token " + os.getenv("GITHUB_TOKEN"),
    "Accept": "application/vnd.github+json"
}

try:
    r = requests.post(os.getenv("GITHUB_URL") + "/user/repos", data=payload, headers=headers)
    r.raise_for_status()
except requests.exceptions.RequestException as err:
    raise SystemExit(err)

try:
    os.chdir(os.getenv("REPO_PATH"))
    os.system("mkdir " + repo_name)
    os.chdir(os.getenv("REPO_PATH") + repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + os.getenv("GITHUB_USER") + "/" + repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push origin main")
    os.system("code .")
except FileExistsError as err:
    raise SystemExit(err)   
