import requests


def get_repository(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code == 200:
        print("Repository found successfully.")
        return response.json()

    elif response.status_code == 404:
        print("Repository not found.")
        return None

    elif response.status_code == 403:
        print("Access forbidden or API rate limit exceeded.")
        return None

    else:
        print(f"GitHub API error: {response.status_code}")
        return None


repository = get_repository("microsoft", "this-repository-does-not-exist")

if repository is not None:
    print(repository)