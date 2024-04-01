Программа представляет собой веб-приложение на базе Django, которое обрабатывает информацию о пропусках и посещениях в хранилище банка. Вот общая инструкция по тому, что делает программа в целом и как ее запустить:

1. **Функциональность программы:**
   - Охранники могут просматривать информацию о пропусках и посещениях.
   - Есть две основные страницы:
     - Страница информации о пропуске (`passcard_info.html`), где пользователь может увидеть информацию о своих посещениях.
     - Страница хранения информации (`storage_information.html`), которая показывает незакрытые посещения в хранилище.

2. **Запуск программы:**
   - У вас должен быть установлен Python и Django.
   - После клонирования репозитория или загрузки файлов вашего проекта на локальный компьютер перейдите в корневую директорию проекта.
   - Запустите виртуальное окружение (если вы используете).
   - Убедитесь, что все зависимости установлены. Если вы используете `pip`, вы можете установить их, выполнив команду `pip install -r requirements.txt`, если такой файл присутствует в вашем проекте.
   - Необходимо в файле .env прописать настройки для базы данных .
   - Запустите локальный сервер Django с помощью команды `python manage.py runserver`.
   - После запуска сервера вы сможете открыть веб-браузер и перейти по URL-адресам, указанным в вашем файле `urls.py`, чтобы просмотреть страницы приложения.

3. **Использование программы:**
   - После запуска сервера вы можете открыть браузер и перейти по адресу, указанному в выводе команды `runserver` (обычно `http://127.0.0.1:8000/`).
   - Перейдите на страницы, которые вам интересны, используя URL-адреса, указанные в вашем файле `urls.py`.
   - На странице информации о пропуске (`passcard_info.html`) вы можете ввести номер пропуска и узнать информацию о посещениях этим пропуском.
   - На странице хранения информации (`storage_information.html`) вы можете увидеть незакрытые посещения на складе.
