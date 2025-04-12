# test_api6
# Тестирование GitHub API

Автоматизированный тест для работы с репозиториями GitHub через API.

## 📌 Требования
- Python 3.7+
- GitHub аккаунт
- Personal Access Token (с правами `repo`)

## 🛠 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/PolinaCherry12/test_api6
   cd test_api6
   ```

2. Установите зависимости в командной строке:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте свой токен:
   ```ini
   #GITHUB_USER=PolinaCherry12
   #GITHUB_TOKEN=ВАШ_ТОКЕН
   #REPO_NAME=test-repo-1
   ```

## 🚀 Запуск теста
![image](https://github.com/user-attachments/assets/e6cc32c3-1016-4e38-9fcc-e5ae95ac10a1)


## 📝 Как получить токен?
1. Перейдите: `Settings` → `Developer settings` → `Personal access tokens`
2. Создайте токен с правами:
   - `repo` (полный доступ к репозиториям)
   - `delete_repo` (для удаления)
3. Скопируйте токен 
![image](https://github.com/user-attachments/assets/632ef974-f3b4-4a60-aa42-62e945e7bd18)


## 🔍 Пример успешного выполнения
![image](https://github.com/user-attachments/assets/8763e79f-526a-4270-9eae-8cb7e9d99468)

