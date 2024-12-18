# 2 Лабораторная (обычная)
## 1. Задачи
- Написать “плохой” Dockerfile, в котором есть не менее трех “bad practices” по написанию докерфайлов
- Написать “хороший” Dockerfile, в котором эти плохие практики исправлены
- Оописать каждую из плохих практик в плохом докерфайле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат
- Описать 2 плохих практики по работе с контейнерами. ! Не по написанию докерфайлов, а о том, как даже используя хороший докерфайл можно накосячить именно в работе с контейнерами.

## 2. Ход работы
### 2.1. "Плохой" Dockerfile (Dockerfile_bad)
В "плохом" Dockerfile присутсвуют следующие "bad practices"
- Использование тега `latest`. Если использовать данный тег для базового образа, то при каждой повторной сборке контейнира будет загружаться последнияя версия образа, которая скорее всего через некоторое время измениться, и из-за чего, когда последняя версия измениться может возникнуть ошибки несовместимости.
- Хранение секретов прямо в Dockerfile. В данном примере в файле `Dockerfile_bad` были установлены переменные среды для подключения к бд: `ENV UserDb="UserDb"` `ENV PasswordDb="PasswordDb"`, жесткое задание данных значений в Dockerfile ведет к проблемам с безопасностью и конфиденциальностью данных.
- Выполнение команд от пользователя root. Это дает слишком большие возможности для Docker контейнера, и что может подорвать безопасность приложения.

### 2.2. "Хороший" Dockerfile (Dockerfile_good)
- Использовать конкретную версию образа, например, как в файле `Dockerfile_good`: `mcr.microsoft.com/dotnet/aspnet:8.0`
- Передавать информацию о "секретах" при запуске docker контейнера: `docker run -e UserDb="UserDb" -e PasswordDb="PasswordDb" app`
- Использовать специального отличного от root пользователя внутри контейнера, например, как в файле `Dockerfile_good`: `USER app`

### 2.3. Плохие практики по работе с контейнерами.
- Использование Docker контейнеров как виртуальных машин. Это проявляется в том, что может появиться нужда в подключению к контейнеру через ssh и "что-то" обновить, или вытащить вручную файлы/логи. Это присуще виртуальным машинам, но не контейнерам. Docker контейнеры должны быть легковесными и не должны использоваться для хранения данных.
- Не хранить данные в контейнерах, так как контейнер может быть остановлен, удален или заменен.




# 2 Лабораторная (*)
## 1. Задачи
- Написать “плохой” Docker compose файл, в котором есть не менее трех “bad practices” по их написанию
- Написать “хороший” Docker compose файл, в котором эти плохие практики исправлены
- Описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат
- Настроить сервисы так, чтобы контейнеры в рамках этого compose-проекта так же поднимались вместе, но не "видели" друг друга по сети.


## 2. Ход работы
### 2.1. "Плохой" docker-compose.yml (docker-compose_bad.yml)
В "плохом" docker-compose.yml  присутсвуют следующие "bad practices"
- Использование тега `latest` для сервиса db. Проблема аналогичная той, которая встречается при использовании этого тега в Dockerfile, а имено потеря контроля над версиями, и возможные ошибки несовместимости версий.
- Хранение секретов прямо в docker-compose.yml. В данном примере в файле `docker-compose_bad.yml` используются переменые среды для подключения к бд, что влечет к проблемам с безопасностью.
- Отсутствия проверки на работоспособность других контейнеров у тех, которые от них зависят, другими словами отсутствие `depends_on` выражения, в данном случае от сервиса `db`.

### 2.2. "Хороший" docker-compose.yml (docker-compose_good.yml)
- Использовать конкретную версию образа, например, как в файле `docker-compose_good.yml` для сервиса db: `postgres:17`
- Передавать информацию о "секретах" с помощью дополнительного файлв .env.
- Указавать выражение `depends_on` для сервисов, которые зависят от других, в данном случае указать для `web-first` и `web-second`.

### 2.3. Изоляция сервисов
Для изоляции сервисов `web-first`, `web-second` и `db` нужно для каждого сервиса создать отдельную сеть - `network`. В docker-compose_good.yml были созданы 3 сети: db-net, web-first-net и web-second-net для сервисов  db, web-first и web-second аналогично. (рисунок 1)

![image](https://github.com/user-attachments/assets/cbe03139-7913-4388-ae39-6930732c6d6b)

Рисунок 1 - Networks

Потом для каждого сервиса была указана своя сеть, что и позволило изолировать данные сервисы.
