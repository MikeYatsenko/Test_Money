# Test_Money

БД - PostgreSQL

в файле settings.py все настройки есть
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'ceapp', 'USER' : 'admin', 'PASSWORD' : 'v320', 'HOST' : 'localhost', 'PORT' : '5432', } }

Запуск кода:


Выполнить миграции:
mysite>python manage.py migrate

Создать суперюзера:
mysite>python manage.py createsuperuser

Запустить сервер:
mysite>python manage.py runserver

Tecты находятся в папке tests

Фронт, как я понимаю, был не главным, поэтому прошу извинить за неряшность. При необходимости, сайт будет выглядеть значительно красивее.
