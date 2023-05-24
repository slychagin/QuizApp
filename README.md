# quiz_app
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
- протестировано с помощью pytest.

#
#### Что использовано для создания API:
- вэб сервис реализован на Python3 с помощью FastAPI;
- в качестве СУБД использована PostgreSQL;
- вэб сервис разворачивается в Docker с помощью docker compose.

#
#### Пример запроса к POST API сервиса в документации Swagger:
POST запрос к API:

![post](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/POST%20request.gif)

Проверяем базу данных в pgadmin:

![check db](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/check%20db.gif)

Аутентификация пользователя:

![auth](https://github.com/slychagin/QuizApp/blob/master/demo_gifs/Authentication.gif)

#
#### Инструкция по настройке и запуску приложения:
- для выполнения данных инструкций у вас должен быть установлен Docker;
- в коммандной строке откройте папку, в которую хотите склонировать проект и запустите команду
`git clone https://github.com/slychagin/QuizApp.git`;
- затем перейдите в корневую папку проекта `cd QuizApp`;
- создайте образ Docker `docker compose build`;
- запустите контейнеры `docker compose up` (после выполнения данной команды у вас должны запуститься следующие сервисы: само приложение, база данных postgres и pgadmin);
- 








