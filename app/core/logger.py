import logging

# Формат рядка логування:
# %(asctime)s - час події
# %(levelname)s - рівень логування (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# %(name)s - ім'я логгера
# %(message)s - текст повідомлення
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# Конфігурація логування
logging.basicConfig(
    level=logging.DEBUG,  # Мінімальний рівень логування (DEBUG для девелопменту, INFO для продакшн)
    format=LOG_FORMAT,    # Використання заданого формату
    handlers=[
        logging.StreamHandler(),            # Вивід логів у консоль
        logging.FileHandler("logs/app.log", encoding="utf-8")  # Запис логів у файл з кодуванням UTF-8
    ]
)

# Ініціалізація логгера з іменем "app"
logger = logging.getLogger("app")
