import os

# Базова директорія
UPLOAD_DIR = "media/lessons_first"

# Піддиректорії
LETTER_IMG_SUBDIR = "letter_images"
OBJECT_IMG_SUBDIR = "object_images"
AUDIO_SUBDIR = "audio"

# Повні шляхи (на випадок потреби)
LETTER_IMG_DIR = os.path.join(UPLOAD_DIR, LETTER_IMG_SUBDIR)
OBJECT_IMG_DIR = os.path.join(UPLOAD_DIR, OBJECT_IMG_SUBDIR)
AUDIO_DIR = os.path.join(UPLOAD_DIR, AUDIO_SUBDIR)
