import requests


def get_repository(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    print(response.status_code)

    return response.json()


repository = get_repository("microsoft", "vscode")

print(repository)