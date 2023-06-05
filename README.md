# QuizApp
![made by](https://img.shields.io/badge/made_by-slychagin-orange)
![python](https://img.shields.io/badge/python-v3.10.5-blue)
![fastapi](https://img.shields.io/badge/fastapi-v0.95.1-green)
![fastapi-users](https://img.shields.io/badge/fastapi_users-v11.0.0-red)
![postgres](https://img.shields.io/badge/postgres-15-blue)
![pytest](https://img.shields.io/badge/pytest-ok-brightgreen)

API  that allows you to save questions for quizzes to the database
#
#### Функционал вэб сервиса:
Веб сервис на Python3 (фреймворк FastAPI), выполняющий следующие функции:
- реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer};
- после получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 
указанное в полученном запросе количество вопросов;
- далее полученные ответы сохраняются в базу данных Postgres, в случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются
дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины;
- также реализована аутентификация пользователей;
- протестировано с помощью pytest;
- Кроме стандартной документации Swagger, так же реализован фронтенд.

#
#### Что использовано для создания API:
- вэб сервис реализован на Python3 с помощью FastAPI;
- в качестве СУБД использована PostgreSQL;
- вэб сервис разворачивается в Docker с помощью docker compose.

#
#### Пример запроса POST к API сервиса (фронтенд):
POST запрос к API:

![front_upload](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/front_upload.gif)


#
#### Пример запроса POST к API сервиса (документациz Swagger):
POST запрос к API:

![post](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/post_request.gif)

Проверяем базу данных в pgadmin:

![check db](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/check_db.gif)

Аутентификация пользователя:

![auth](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/Authentication.gif)

#
#### Инструкция по настройке и запуску приложения:
- для выполнения данных инструкций у вас должен быть установлен Docker;
- все данные для подключения есть в файле .env-prod (так как приложение тестовое, то данный файл не добавлял в .gitignore);
- в коммандной строке откройте папку, в которую хотите склонировать проект и запустите команду

`git clone https://github.com/slychagin/QuizApp.git`;
- затем перейдите в корневую папку проекта `cd QuizApp`;
- создайте образ Docker `docker compose build`;
- запустите контейнеры `docker compose up` (после выполнения данной команды у вас должны запуститься следующие сервисы: приложение, база данных postgres и pgadmin);
- - чтобы зайти в приложение через фронтенд посетите адрес `http://localhost:9999`, документация Swagger - зайдите по адресу `http://localhost:9999/docs`;
- в документации вы можете попробовать зарегистрировать пользователя, залогиниться, выполнить POST запрос к API согласно примерам выше (аутентификация добавлена, но для ускорения процесса, чтобы не надо было логиниться, отключена. При необходимости решается раскомментированием одной строчки в коде);
- для работы с базой данных в удобном интерфейcе Pgadmin4 необходимо зайти по адресу `http://localhost:5050`, аутентифицироваться введя почту `quiz@quiz.com` и пароль `quiz_777`:

![pgadmin_auth](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/pgadmin_auth.jpg)
- далее создайте новый сервер:

![pgadmin_create_server](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/pgadmin_create_server.jpg)
- в открывшемся окне во вкладке General введите любое имя для сервера:

![pgadmin_enter_name](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/pgadmin_enter_name.jpg)
- в том же окне во вклдаке Connection заполните Host name/address=postgres_container, Port=5432, Maintenance database=postgres, Username=postgres, Password=postgres и нажмите Save, чтобы подключиться к серверу. Как вариант, в Host name/address можно ввести не имя контейнера Postgres, а IP адрес. Для чего в командной строке выполните команды `docker ps` -> скопируйте ID или имя контейнера Postgres -> `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id`:

![pgadmin_connection](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/pgadmin_connection.jpg)
- чтобы просмотреть, добавленные в базу данных записи выполните запрос `SELECT * FROM questions;`

![pgadmin_get_data](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/pgadmin_get_data.jpg)
