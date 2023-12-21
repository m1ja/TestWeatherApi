## Шаг 1: Установка зависимостей

1. Убедитесь, что у вас установлен Python 3.x.
2. Создайте виртуальное окружение:

   ```bash
   python -m venv venv

3. Активируйте виртуальное окружение:

   - Для Windows:

     ```bash
     venv\Scripts\activate
     ```

   - Для Unix или MacOS:

     ```bash
     source venv/bin/activate
     ```

4. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   
## Шаг 2: Настройка базы данных Django

1. Выполните миграции Django:

    ``` bash
    python manage.py migrate
   
2. Создайте административного пользователя:

    ```bash
    python manage.py createsuperuser
   
## Шаг 3: Запуск Django-приложения
1. Запустите Django-приложение:

    ```bash
    python manage.py runserver
   
Проверьте доступность веб-приложения в вашем веб-браузере по адресу http://127.0.0.1:8000/.

Перейдите в админ-панель Django (http://127.0.0.1:8000/admin/) и войдите, используя созданные учетные данные.

## Шаг 4: Запуск телеграм-бота
1. Запустите телеграм-бота:

    ```bash
    python telegram_bot.py
   
## Шаг 5: Тестирование
Убедитесь, что веб-приложение и телеграм-бот работают корректно.

**Примечание:**

Убедитесь, что у вас есть X-Yandex-API-Key (API-ключ) от Yandex Weather API и укажите его в соответствующем месте в коде.