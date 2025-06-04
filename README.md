# 📚 Лісова Абетка – Бекенд

Бекенд частина освітнього вебдодатку **"-Лісова абетка: Рукавичка"**, створеного для навчання дітей української абетки. Реалізовано за допомогою **FastAPI**, з підтримкою авторизації, уроків, прогресу користувача та завантаження медіафайлів.

## 📁 Структура проєкту

```
backend/
├── app/
│   ├── api/v1/routes/          # Роути (auth, users, lessons, progress)
│   ├── core/                   # Конфігурація, безпека
│   ├── db/                     # Підключення до БД
│   ├── models/                 # SQLAlchemy моделі
│   ├── schemas/                # Pydantic-схеми
│   ├── services/               # Бізнес-логіка
│   └── main.py                 # Точка входу FastAPI
├── tests/                      # Юніт-тести
├── Dockerfile                  # Docker-інструкції
├── requirements.txt            # Залежності
└── .env                        # Конфігураційні змінні
```

## 🚀 Запуск проєкту

### 🔧 Встановлення локально

1. Клонуй репозиторій:

   ```bash
   git clone https://github.com/your-username/lisova-abetka-backend.git
   cd lisova-abetka-backend/backend
   ```

2. Створи `.env` файл (div. нижче).

3. Створи та активуй віртуальне середовище:

   ```bash
   python -m venv venv
   source venv/bin/activate   # або venv\Scripts\activate на Windows
   ```

4. Встанови залежності:

   ```bash
   pip install -r requirements.txt
   ```

5. Запусти FastAPI-сервер:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Відкрий Swagger-документацію:

   ```
   http://localhost:8000/docs
   ```

---

## 🐳 Docker запуск

1. Запусти Docker-контейнери:

   ```bash
   docker-compose build backend
   docker-compose up --build
   docker-compose down

   ```
  ```bash
  docker exec -i postgres-db psql -U postgres -c "\l" <----список
  docker exec -i postgres-db psql -U postgres -c "CREATE DATABASE mydatabase;"
  
  docker exec -i postgres-db psql -U postgres -c "DROP DATABASE mydatabase;"
  docker exec -i postgres-db psql -U postgres -d postgres -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

  docker exec -i postgres-db psql -U postgres -d postgres < postgres_localhost-2025_05_21_23_21_12-dump.sql  <----в базу
  docker exec -t postgres-db pg_dump -U postgres -d postgres > backup.sql  <----c бази
  ```
---

## ⚙️ Приклад `.env` файлу

```
DATABASE_URL=postgresql://user:password@localhost:5432/abetka_db
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
UPLOAD_FOLDER=app/static/uploads
```

---

## 🔐 Авторизація

* Реєстрація: `POST /api/v1/auth/register`
* Логін: `POST /api/v1/auth/login`
  Повертається JWT-токен, який потрібно передавати в `Authorization: Bearer <token>`.
* юзери за замовчуванняям
{
  "username": "testuser1",
  "email": "testuser1@example.com",
  "password": "testpassword1"
}

{
  "username": "testadmin1",
  "email": "testadmin1@example.com",
  "password": "testpassword1"
}
---

## 📚 Основні роутери

| Метод  | Endpoint                      | Опис                           |
| ------ | ----------------------------- | ------------------------------ |
| `POST` | `/api/v1/auth/register`       | Реєстрація користувача         |
| `POST` | `/api/v1/auth/login`          | Вхід користувача               |
| `GET`  | `/api/v1/users/me`            | Дані текущого користувача      |
| `POST` | `/api/v1/lessons/`            | Створення уроку з медіафайлами |
| `GET`  | `/api/v1/lessons/{lesson_id}` | Отримання уроку                |
| `POST` | `/api/v1/progress/`           | Збереження прогресу            |
| `GET`  | `/api/v1/progress/`           | Отримання прогресу користувача |

---

## 🥮 Тестування

```bash
pytest tests/
```

---

## 📂 Завантаження медіафайлів

* Підтримується одночасне завантаження зображень, аудіо та JSON-квізу при створенні уроку.
* Файли зберігаються у папці `app/static/uploads/`.
* Шляхи до файлів автоматично додаються до бази даних.

---

## 📄 Ліцензія

MIT License.
Copyright (c) 2025 Oleksii Tkachenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---

## 📬 Контакти

> Розробник: **Oleksii Tkachenko**


