# TronWalletServiceAPI

Это API для управления информацией о кошельках Tron, позволяющее пользователям добавлять и получать информацию о кошельках. Проект включает в себя функциональность для проверки баланса, энергии и пропускной способности.

## Особенности
- Интеграция с базой данных для постоянного хранения
- Хорошо структурированные эндпоинты API для легкого доступа к ресурсам
- Пример проектирования проекта (хоть это и не особо актуально в рамках данного проекта) с применением различных паттернов (service, repository и т.д.)
- Тестирование для обеспечения надежности

## Установка

1. Клонируйте репозиторий, находясь в директории, куда хотите скачать проект:
   ```bash
   git clone https://github.com/s0wll/TronWalletServiceAPI.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd TronWalletServiceAPI
   ```
3. В корне проекта создайте файл .env и установите в нем следующие значения:
    ```bash
    MODE=LOCAL

    DB_HOST=tron_wallet_db
    DB_PORT=5432
    DB_USER=tron_wallet_user
    DB_PASS=tron_wallet_password
    DB_NAME=TronWalletServiceAPI
    ```

## Запуск

Запустите Docker Compose с помощью следующей команды:
```bash
docker compose up --build
```

Для запуска приложения только с логами API, вместо команды выше выполните:
```bash
docker compose up -d --build
```
```bash
docker logs --follow library_back
```

## Документация

API документация доступна по адресу: http://localhost/docs

## Тестирование

1. Для проведения тестирования, в корне проекта необходимо создать дополнительный файл .env-test и установить в нем следующие значения:
   ```bash
   MODE=TEST

   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=(ваше имя пользователя postgres)
   DB_PASS=(ваш пароль postgres)
   DB_NAME=TronWalletServiceAPI-test
   ```

2. Далее создайте дополнительную базу данных в PostgreSQL и назовите ее        "TronWalletServiceAPI-test"

3. Далее создайте и запустите виртуальное окружение с помощью команд (Я использовал в разработке версию Python 3.13.1):
   ```bash
   python3 -m venv venv
   ```

   Для MacOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   Для Windows:
   ```bash
   venv\Scripts\activate.bat
   ```
   
   Не забудьте выбрать правильное venv в вашем редакторе кода (В случае с VSCode - это "Recommended").

4. Далее скачайте зависимости, выполнив команду:
   ```bash
   pip install -r requirements.txt
   ```

После этого, для запуска тестирования, выполните следующую команду:
```bash
pytest -v -s
```

Если возникнут проблемы с переменными окружения, то выполните следующие команды, чтобы сбросить их значения:
```bash
unset MODE
unset DB_HOST
unset DB_PORT
unset DB_USER
unset DB_PASS
unset DB_NAME
```
