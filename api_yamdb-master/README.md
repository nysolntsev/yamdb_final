# Описание

Проект YaMDb, который собирает отзывы пользователей на произведения
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

4) Выполнить миграции
```
python3 manage.py migrate
```

5) Запустить сервер
```
python3 manage.py runserver
```

# Авторы
https://github.com/Hauda15 написал часть, касающуюся управления пользователями (Auth и Users): систему регистрации и аутентификации, права доступа, работу с токеном, систему подтверждения через e-mail.
https://github.com/nysolntsev написал категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них.
https://github.com/DUProkofev написал часть, касающуюся отзывов (Review) и комментариев (Comments): описывал модели, представления, настроил эндпойнты, определил права доступа для запросов, а также настроил рейтинги произведений.

