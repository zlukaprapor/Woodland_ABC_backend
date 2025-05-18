import os
from PIL import Image

def resize_images_in_folder(input_folder: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)

            try:
                with Image.open(input_path) as img:
                    img_resized = img.resize((300, 300))
                    img_rgb = img_resized.convert('RGB')
                    img_rgb.save(output_path, format='PNG')
                    print(f"✅ Оброблено: {filename} → {output_filename}")
            except Exception as e:
                print(f"❌ Помилка з {filename}: {e}")

# Отримуємо абсолютний шлях до поточної папки скрипта
base_dir = os.path.dirname(os.path.abspath(__file__))

# Формуємо абсолютні шляхи
input_folder = os.path.join(base_dir, "input_folder")
output_folder = os.path.join(base_dir, "output_images")

resize_images_in_folder(input_folder, output_folder)
