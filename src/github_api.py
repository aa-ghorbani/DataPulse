import json
from pathlib import Path

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


def save_repository(data, filename):
    project_root = Path(__file__).resolve().parent.parent
    raw_dir = project_root / "data" / "raw"

    raw_dir.mkdir(parents=True, exist_ok=True)

    file_path = raw_dir / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Repository data saved to {file_path}")


repository = get_repository("microsoft", "vscode")

if repository is not None:
    save_repository(repository, "microsoft_vscode.json")