# Проект SocialNetwork.02

[![pytest](https://img.shields.io/badge/-pytest-464646?style=for-the-badge&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django)
![HTML5](https://img.shields.io/badge/HTML5-34F26?style=for-the-badge&logo=Html5&logoColor=white)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=for-the-badge&logo=css3)](https://en.wikipedia.org/wiki/CSS)
![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=blue)
![Git](https://img.shields.io/badge/Git-black?style=for-the-badge&logo=Git&logoColor=red)
## Описание

SocialNetwork - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

## Функционал

1. Создано и подключено приложение `core`:

   - размещён и зарегистрирован фильтр `addclass`, позволяющий добавлять CSS - класс к тегу шаблона;
   - создан и зарегистрирован контекст-процессор, добавляющий текущий год на все страницы в переменную `{{ year }}`.

2. Создано и подключено приложение `about`:

   - созданы статические страницы `/about/author/` и `/about/tech/`;
   - ссылки на эти страницы добавлены в навигацию сайта.

3. Подключено приложение `django.contrib.auth`, его `urls.py` подключен к основному `urls.py`.

4. Создано и подключено приложение `users`:

   - переопределены шаблоны для адреса авторизации `/auth/login/`;
   - переопределены шаблоны для адреса выхода из аккаунта `/auth/logout/`;
   - создана страница `/auth/signup/` с формой для регистрации пользователей.

5. В приложении `posts` сделано следующее:

   - создана страница пользователя c постами пользователя `profile/<username>/`;
   - создана отдельная страница поста `posts/<post_id>/`;
   - подключен паджинатор, выводящий по десять постов на страницы профиля, группы и главную.

6. Создана навигация по разделам.

7. Ссылка «Новая запись» добавлена в шапку сайта. Она видна только авторизованным пользователям и ведёт на страницу `/create/`.

8. На странице `/create/` создана форма для добавления новой публикации:
   - view-функция для страницы `/create/` называется `post_create()`;
   - name для `path()` страницы `/create/ - post_create`;
   - в контекст шаблона страницы /create/ передается переменная form. Она содержит объект `PostForm`, в котором два поля:
   - `text` (обязательное для заполнения поле);
   - `group` (необязательное для заполнения);
   - после валидации формы и создания нового поста автор перенаправляется на страницу своего профайла `/profile/`.
9. Добавлена страница редактирования записи с адресом `/posts/<post_id>/edit/`. View-функцию для этой страницы `post_edit()`.
   - Права на редактирование есть только у автора этого поста. Остальные пользователи перенаправляются на страницу просмотра поста.
   - При генерации страницы в контекст передается переменная `form`, в ней два поля: `text` и `group`.
   - Для страницы редактирования поста применяется тот же HTML - шаблон, что и для страницы создания нового поста: `posts/create_post.html`.
10. Шаблон усложнен:
    - при редактировании поста заголовок «Добавить запись» заменяется на «Редактировать запись»;
    - надпись на кнопке отправки формы зависит от операции: «Добавить» для новой записи и «Сохранить» — для редактирования.

## Установка

1. Клонировать репозиторий:

    ```python
    git clone https://github.com/egorcoders/hw02_community.git
    ```

2. Перейти в папку с проектом:

    ```python
    cd socialnetwork02/
    ```

3. Установить виртуальное окружение для проекта:

    ```python
    python -m venv venv
    ```

4. Активировать виртуальное окружение для проекта:

    ```python
    # для OS Lunix и MacOS
    source venv/bin/activate

    # для OS Windows
    source venv/Scripts/activate
    ```

5. Установить зависимости:

    ```python
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

6. Выполнить миграции на уровне проекта:

    ```python
    cd yatube
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

7. Запустить проект локально:

    ```python
    python3 manage.py runserver

    # адрес запущенного проекта
    http://127.0.0.1:8000
    ```
### __Технологии__
* Python3
* Flake8
* pytest==6.2.5
* HTML5
* Django==2.2.9

### __Автор__
[Екатерина Новикова](https://github.com/katherin-ov)
