import os
# from flask import Flask, request, render_template, send_file, jsonify
import io
import requests
import base64
import uuid
from functions import (
    sentiment_analysis,
    generate_text,
    summarize_text,
    # colorize_photo
)
import gradio as gr

def greet(name):
    return "Hello "+name+"!!"

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

@app.route('/', methods = ['GET', 'POST'])
def index():
    result_text = None
    result_image = None
    error = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'sentiment':
            text = request.form.get('text', '')
            if text:
                result_text = sentiment_analysis(text)
            else:
                error = "Введите текст"

        elif action =="generate":
            prompt = request.form.get('text', '')
            if prompt:
                result_text=generate_text(prompt)
            else:
                error = 'Введите промпт'

        elif action=="summarize":
            text=request.form.get('text', '')
            if text:
                result_text=summarize_text(text)
            else:
                error = "Введите текст для пересказа"

        # # ---------- Функции с фото ----------
        # elif action in ['colorize']:
        #     if 'image' not in request.files:
        #         error = "Файл не загружен"
        #     else:
        #         file = request.files['image']
        #
        #         if file.filename=='':
        #             error= "Файл не выбран"
        #         else:
        #             img_bytes=file.read()
        #             try:
        #                 if action=='colorize':
        #                     # 1 Вызываем функцию раскрашивания
        #                     result_bytes = colorize_photo(img_bytes)
        #
        #                     # 2. Генерируем уникальное имя файла
        #                     filename = f"{uuid.uuid4().hex}.jpg"
        #                     filepath = os.path.join(RESULTS_FOLDER, filename)
        #
        #                     # 3. Сохраняем результат
        #                     with open(filepath, 'wb') as f:
        #                         f.write(result_bytes)
        #
        #                     if os.path.exists(filepath):
        #                         print(f"✅ Файл сохранён: {filepath}, размер: {os.path.getsize(filepath)}")
        #                     else:
        #                         print("❌ Файл не создан!")
        #
        #                     # 4. Передаём URL для отображения
        #                     result_image = f"/static/results/{filename}"
        #                     print("Результат сохранен")
        #                     # encoded = base64.b64encode(result_image=result_image,error=None)
        #                     # return send_file(io.BytesIO(result_bytes), mimetype='image/jpeg')
        #             except Exception as e:
        #                 error = f"Ошибка обработки: {str(e)}"

    return render_template('index.html', result_text=result_text, error=error)

if __name__=='__main__':
    demo.launch(share=True)
    app.run(debug=True, host='0.0.0.0', port=5000)