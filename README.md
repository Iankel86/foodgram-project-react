![https://github.com/Iankel86](https://img.shields.io/badge/Developed%20by-Iankel86-blue) 
![Foodgram Workflow Status](https://github.com/Iankel86/foodgram-project-react/actions/workflows/main.yml/badge.svg?branch=master&event=push)

![](https://img.shields.io/badge/Python-3.7.0-blue?style=flat&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-3.2.15-orange?style=flat&logo=django&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-13.0-blue?style=flat&logo=postgresql&logoColor=white)

## 🍳 Проект Foodgram

**Foodgram** - приложение в котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Foodgram» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

Проект развернут по адресу [84.201.140.81](http://84.201.140.81/)

Адрес электронной почты: yankelll86@mail.ru
Username: admin
Имя пользователя: admin
Фамилия пользователя: admin
Password: 29082022

## ⚙ Используемые технологии:

▪ **Python**<br>
▪ **Django**<br>
▪ **Django Rest Framework**<br>
▪ **Docker**<br>
▪ **Gunicorn**<br>
▪ **NGINX**<br>
▪ **PostgreSQL**<br>
▪ **Yandex Cloud**<br>
▪ **CI/CD**<br>

## 📃 Как развернуть проект на сервере:

Клонировать репозиторий:
```
git@github.com:Iankel86/foodgram-project-react.git
```

Установить на сервере Docker, Docker Compose:

```
sudo apt install curl                                   # установка утилиты для скачивания файлов
curl -fsSL https://get.docker.com -o get-docker.sh      # скачать скрипт для установки
sh get-docker.sh                                        # запуск скрипта
sudo apt-get install docker-compose-plugin              # последняя версия docker compose
```

Скопировать на сервер файлы docker-compose.yml, nginx.conf из папки infra (команды выполнять находясь в папке infra):

```
scp docker-compose.yml nginx.conf <username>@<IP>:/home/<username>/   # username - имя пользователя на сервере
                                                                      # IP - публичный IP сервера
```

Создать файл .env и заполнить своими данными:
```
touch .env
nano .env
```
```а
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=1234567890
```

Создать и запустить контейнеры Docker, выполнить команду на сервере
*(версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):*
```
sudo docker compose up -d
```

После успешной сборки выполнить миграции:
```
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate
```

Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

Наполнить базу данных содержимым из файла ingredients.json:
```
sudo docker compose exec backend python manage.py loaddata ingredients.json
```

### Ураа! Ваш сервер работает! 😸
Не забудьте добавить теги для блюд в админ-панели your-host/admin/
<br><br>


Для остановки контейнеров Docker:
```
sudo docker compose down -v      # с их удалением
sudo docker compose stop         # без удаления
```

Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение
DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

### После каждого обновления репозитория (push в ветку master) будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

### Запуск проекта на локальной машине:

Клонировать репозиторий:
```
git@github.com:Iankel86/foodgram-project-react.git
```

В директории infra файл .env заполнить своими данными:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=1234567890
```

Создать и запустить контейнеры Docker, как указано выше.

После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)

Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)


## Автор проекта:

### Шадрин Ян:
```
e-mail: yankelll86@mail.ru
e-mail: yankelll86@gmail.com
GitHub: https://github.com/Iankel86
```
