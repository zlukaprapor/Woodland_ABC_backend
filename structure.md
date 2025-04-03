Woodland_ABC_backend
lisova-abetka/
│── backend/                  # Папка з бекендом (FastAPI)
│   ├── app/
│   │   ├── api/              # Ендпоінти API
│   │   │   ├── v1/
│   │   │   │   ├── routes/   # Маршрути API
│   │   │   │   │   ├── auth.py  # Реєстрація, логін
│   │   │   │   │   ├── users.py  # Користувачі
│   │   │   │   │   ├── tasks.py  # Завдання для дітей
│   │   │   │   │   ├── progress.py  # Прогрес користувачів
│   │   │   │   ├── __init__.py
│   │   ├── core/             # Основні налаштування
│   │   │   ├── config.py     # Конфігурація (налаштування БД, API-ключів)
│   │   │   ├── security.py   # Авторизація та JWT-токени
│   │   ├── models/           # SQLAlchemy моделі
│   │   │   ├── user.py
│   │   │   ├── task.py
│   │   │   ├── progress.py
│   │   ├── schemas/          # Pydantic-схеми для API
│   │   │   ├── user.py
│   │   │   ├── task.py
│   │   │   ├── progress.py
│   │   ├── services/         # Логіка бізнес-процесів
│   │   │   ├── user_service.py
│   │   │   ├── task_service.py
│   │   │   ├── progress_service.py
│   │   ├── db/               # Робота з базою даних
│   │   │   ├── database.py   # Підключення до БД
│   │   ├── main.py           # Головний файл запуску FastAPI
│   ├── tests/                # Тести для API
│   ├── Dockerfile            # Docker-образ для бекенду
│   ├── requirements.txt      # Список залежностей Python
│   ├── .env                  # Секретні ключі та конфігурації
│── frontend/                 # Папка з фронтендом (React)
│   ├── src/                  # Код React
│   │   ├── components/       # Компоненти інтерфейсу
│   │   ├── pages/            # Сторінки
│   │   ├── api/              # Запити до бекенду
│   │   ├── styles/           # SCSS-стилі
│   ├── public/               # Статичні файли
│   ├── package.json          # Залежності React
│   ├── vite.config.js        # Налаштування Vite (або Webpack)
│── .gitignore                # Файли, які не потрібно комітити
│── docker-compose.yml        # Запуск бекенду + фронтенду через Docker
│── README.md                 # Опис проєкту