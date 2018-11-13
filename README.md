# audit-sugar-utm-2
Web-морда на Django для формирования отчётности из SugarCRM и UTM5. Конфигурация специфическая, так что мало оно кому поможет (во всяком случае в чистом виде).

Это переосмысленная версия audit-sugar-utm.

flask концептуально больше подходит для проекта: работа с внешней легаси базами. Однако для реализации был выбран django, после того как в прототипе на flask дошла очередь реализовывать админку и авторизацию пользователей.

## Особенности реализации

Пришлось отказаться от использования Django ORM при работе с внешними базами (manage.py inspectdb) в связи с тем, что версии БД свежими версиями Django не поддерживается. Поэтому используем sqlalchemy.   

## Docker

```bash
docker build -t audit-sugar-utm:latest .
docker run -it --env-file audit-sugar-utm.env -p 127.0.0.1:8888:8000/tcp audit-sugar-utm:latest
```

Создайте файл audit-sugar-utm.env
```
DJANGO_SECRET_KEY='very-secret-key'
```
Создайте файл postgres.env
```bash
POSTGRES_PASSWORD=ваш_пароль
POSTGRES_USER=пользователь
POSTGRES_DB=имя_БД
```

Запустите docker-compose
```bash
docker-compose up --build
```

После первого запуска, надо инициализировать базу.
```bash
docker exec  -it <id_container> python manage.py migrate
```