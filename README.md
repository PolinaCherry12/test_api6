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

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте токен:
   ```ini
   #GITHUB_USER=PolinaCherry12
   #GITHUB_TOKEN=ВАШ_ТОКЕН
   #REPO_NAME=test-repo-1
   ```

## 🚀 Запуск теста
```bash
python test_api.py6
```

## 📝 Как получить токен?
1. Перейдите: `Settings` → `Developer settings` → `Personal access tokens`
2. Создайте токен с правами:
   - `repo` (полный доступ к репозиториям)
   - `delete_repo` (для удаления)
3. Скопируйте токен (он покажется только один раз!)


## 🔍 Пример успешного выполнения
```
1. Создаю репозиторий...
✅ Репозиторий test-repo-123 создан!
2. Проверяю список репозиториев...
✅ Репозиторий найден в списке.
3. Удаляю репозиторий...
✅ Репозиторий успешно удален.
```
