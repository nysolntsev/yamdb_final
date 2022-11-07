# Описание

Проект YaMDb, который собирает отзывы пользователей на произведения

![example workflow](https://github.com/nysolntsev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Установка

1) Склонировать репозиторий
```
git clone https://github.com/nysolntsev/api_final_yatube.git
```
2) Создать и активировать виртуальное окружение для проекта

```
python3 -m venv venv
```
```
source venv/bin/activate
```

3) Установить зависимости
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

4) Создайте файл .env с переменными окружения для работы с базой данных
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```

6) Запустите docker-compose
```
docker-compose up -d --build 
```
7) Выполните по очереди команды
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
8) Запустите docker-compose
```
docker-compose up -d --build 
```
9) Перейдите по адресу и введите данные созданного супер пользователя
```
http://localhost/admin/
```

# Авторы
https://github.com/Hauda15 написал часть, касающуюся управления пользователями (Auth и Users): систему регистрации и аутентификации, права доступа, работу с токеном, систему подтверждения через e-mail.
https://github.com/nysolntsev написал категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них.
https://github.com/DUProkofev написал часть, касающуюся отзывов (Review) и комментариев (Comments): описывал модели, представления, настроил эндпойнты, определил права доступа для запросов, а также настроил рейтинги произведений.

