import logging
# Формат логування

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
logging.basicConfig(
level=logging.DEBUG, # Можна змінити на INFO для продакшну
format=LOG_FORMAT,
handlers=[
logging.StreamHandler(), # Вивід у консоль
logging.FileHandler("logs/app.log", encoding="utf-8")]) # Логи вфайл

logger = logging.getLogger("app")