import os
from flask import Flask, request, render_template, session, send_file, jsonify
import io
import requests
import base64
import uuid
from functions import (
    sentiment_analysis,
    generate_text,
    summarize_text,
    chat_with_agent,
    text_stats,
    paraphrase_text
)
import traceback

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))

@app.route('/', methods = ['GET', 'POST'])
def index():
    result_text = None
    error = None
    chat_history = session.get('chat_history', [])

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

        elif action=="chat":
            pass

        elif action =="stats":
            text=request.form.get('text','')
            if text:
                result_text = text_stats(text)
            else:
                error="Введите текст"

        elif action =="paraphrase":
            text=request.form.get('text','')
            if text:
                result_text = paraphrase_text(text)
            else:
                error="Введите текст"

    return render_template('index.html',
                           result_text=result_text,
                           error=error,
                           chat_history=chat_history)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    """AJAX - эндпоинn для общения с ИИ - агентом."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Неверный запрос'}), 400
        user_message=data.get('message', '').strip()
        if not user_message:
            return jsonify({'error':'сообщение не может быть пустым'}), 400

        history = session.get('chat_history',[])
        reply, new_history=chat_with_agent(history, user_message)
        session['chat_history']=new_history
        return jsonify({'reply':reply})
    except Exception as e:
        print(f"❌ Ошибка в /chat: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__=='__main__':

    app.run(debug=True, host='0.0.0.0', port=7860)