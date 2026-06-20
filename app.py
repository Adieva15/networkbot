import os
from flask import Flask, request, render_template, send_file, jsonify
import io
from functions import (
    sentiment_analysis,
    generate_text,
)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
    return render_template('index.html', result_text=result_text, error=error)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)