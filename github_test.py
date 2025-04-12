import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USER = os.getenv('GITHUB_USER')
REPO_NAME = os.getenv('REPO_NAME', f"test-repo-{int(time.time())}")  

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_github_repo_workflow():
    try:
        # 1. Создание репозитория
        print("1. Создаю репозиторий...")
        response = requests.post(
            "https://api.github.com/user/repos",
            json={"name": REPO_NAME, "auto_init": True},
            headers=headers
        )
        response.raise_for_status()  # Проверка ошибок
        print(f"✅ Репозиторий {REPO_NAME} создан!")

        # 2. Проверка существования
        print("2. Проверяю список репозиториев...")
        response = requests.get(
            f"https://api.github.com/users/{GITHUB_USER}/repos",
            headers=headers
        )
        repos = [repo["name"] for repo in response.json()]
        assert REPO_NAME in repos, "Репозиторий не найден в списке!"
        print("✅ Репозиторий найден в списке.")

        # 3. Удаление
        print("3. Удаляю репозиторий...")
        response = requests.delete(
            f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}",
            headers=headers
        )
        assert response.status_code == 204, "Ошибка удаления!"
        print("✅ Репозиторий успешно удален.")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        raise

if __name__ == "__main__":
    test_github_repo_workflow()
