# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список категорий (Category) может быть расширен.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории "Книги" могут быть произведения "Винни Пух и все-все-все" и "Марсианские хроники", а в категории "Музыка" — песня "Давеча" группы "Насекомые" и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, "Сказка", "Рок" или "Артхаус"). Новые жанры может создавать только администратор.
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг.

# Примеры запросов
Регистрация нового пользователя:
POST api/v1/auth/signup/
Получение JWT-токена:
POST api/v1/auth/token/
Получение списка всех категорий:
GET api/v1/categories/
Удаление жанра:
DELETE api/v1/genres/{slug}/
Частичное обновление информации о произведении:
PATCH /api/v1/titles/{titles_id}
Получение списка всех отзывов:
GET /api/v1/titles/{title_id}/reviews/
Добавление комментария к отзыву:
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

# Установка
Склонируйте репозиторий. Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `source venv\scripts\activate`; Linux/Mac: `sorce venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.

Для запуска сервера разработки,  находясь в директории проекта выполните команды:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Проект запущен и доступен по адресу [localhost:8000](http://localhost:8000/).

# Технологии
Python 3.7
Django 3.2
Django Rest Framework 3.12.4
Simple JWT
SQLite3

# Авторы
Данилова Марина - https://github.com/maridana
Личинин Виталий - https://github.com/Lichinin
Горовенко Валентин - https://github.com/ValentinGorovenko
