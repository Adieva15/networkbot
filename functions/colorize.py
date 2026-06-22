import os
import numpy as np
import cv2
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from huggingface_hub import snapshot_download
from pathlib import Path
import tempfile

# Путь к локальной папке с моделью (загрузится один раз при первом вызове)
MODEL_DIR=Path('./makeitcolor')
MODEL_REPO='muhammadnoman76/makeitcolor'

# Глобальный пайплайн (загружается один раз)
_pipeline=None

def _get_pipeline():
    global _pipeline
    if _pipeline is None:
        if not MODEL_DIR.exists():
            print('Модель скачивается, это займет около 300 Мб.')
            snapshot_download(repo_id=MODEL_REPO, local_dir=str(MODEL_DIR), repo_type="model")
            print('Модель загружена.')
        # Initialize the colorization pipeline
        _pipeline=pipeline(Tasks.image_colorization,  model=str(MODEL_DIR))
    return _pipeline

def colorize_photo(image_bytes:bytes)->bytes:
    """
    Принимает байты чёрно-белого изображения,
    возвращает байты раскрашенного изображения (JPEG).
    """
    try:
        # Сохраняем входное изображение во временный файл
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_in:
            tmp_in.write(image_bytes)
            tmp_in_path = tmp_in.name

        # Запускаем раскрашивание
        pipe = _get_pipeline()
        result=pipe(tmp_in_path)# возвращает dict с ключом 'output_img'

        # Получаем результат (numpy array) и конвертируем в байты JPEG
        output_img=result['output_img']# это numpy array (H, W, 3) в BGR

        # Если изображение в BGR, переводим в RGB для правильного сохранения
        # (обычно modelscope возвращает BGR, но проверим)
        if output_img.shape[2]==3:
            output_img=cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

        # Кодируем в JPEG и возвращаем байты
        success, encoded=cv2.imencode('.jpg', output_img)
        if not success:
            raise RuntimeError("Не удалось закодировать изображение")

        # Удаляем временный файл
        os.unlink(tmp_in_path)

        return encoded.tobytes()

    except Exception as e:
        return RuntimeError(f"ошибка раскрашивания: {str(e)}")


