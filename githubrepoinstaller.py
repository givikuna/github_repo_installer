import requests
import os
import subprocess

ACCESS_TOKEN = input('your access token: ').replace(' ', '').replace('\t', '').replace('\n', '')

def get_github_repositories():
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    if response.status_code == 200: return response.json()
    else: raise Exception(f"Failed to fetch repositories. Status code: {response.status_code}")

def clone_github_repositories(repositories):
    for repo in repositories:
        clone_url = repo['clone_url']
        repo_name = repo['name']
        try:
            subprocess.run(['git', 'clone', clone_url, repo_name], check=True)
            print(f"Cloned: {repo_name}")
        except subprocess.CalledProcessError:
            print(f"Failed to clone: {repo_name}")

try:
    repositories = get_github_repositories()
    clone_github_repositories(repositories)
except Exception as e:
    print(f"Error: {e}")
