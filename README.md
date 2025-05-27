# HW-Django
Home Work Python Django

## Предварительные требования
- Python 3.11
- PostgreSQL >=14


## Настройка окружения
```
# Подготовка окружения
pip install poetry
poetry install

# Настройка БД PostgreSQL:
# Создать пользователя для работы с БД
sudo -u postgres psql -c "
CREATE USER [имя_пользователя] WITH ENCRYPTED PASSWORD '[пароль]';
"

# Создать БД с имением magazine
sudo -u postgres psql -c "CREATE DATABASE magazine;"

# Настроить доступ к БД для пользователя
sudo -u postgres psql -c "
ALTER DATABASE magazine OWNER TO [имя_пользователя];
GRANT ALL PRIVILEGES ON DATABASE magazine TO [имя_пользователя];
"

# Создать файл .env на основе .env.sample
# Заполнить значения переменных .env
```

## Запуск проекта
```
# Запуск сервера
poetry run ./manage.py runserver
```
