import os
from openai import OpenAI

HF_TOKEN=os.getenv("HF_TOKEN","")
if not HF_TOKEN:
    raise ValueError("Переменная окружения HF_TOKEN не установлена")
model_chat="zai-org/GLM-5.2:novita"

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)
system_prompt=('Ты — дружелюбный собеседник. Отвечай кратко, по делу, живым русским языком.'
                'Твои ответы — не более 512 символов (включая пробелы).'
                'Избегай воды, повторов и вступлений. Говори суть.'
                'Если вопрос сложный — дай один чёткий совет, а не лекцию.'
                'Считай символы перед отправкой и ужимай ответ при превышении.')

def chat_with_agent(history, user_message):
    if not history:
    # Инициализируем историю с системным сообщением
        history = [
        {"role": "system", "content": system_prompt}
        ]
    # Добавляем сообщение пользователя в историю
    history.append({"role":"user","content":user_message})
    try:
        print("Чат запущен. Введите 'exit' для выхода.\n")
        while True:
            user_input = input("Вы: ")
            if user_input.lower() == "exit":
                break

            # Отправляем всю историю в модель
            completion = client.chat.completions.create(
                model=model_chat,
                messages=history
            )

            # Получаем ответ ассистента
            assistant_message = completion.choices[0].message
            reply = assistant_message.content

            # Добавляем ответ ассистента в историю
            history.append({"role": "assistant", "content": reply})
            return reply, history
    except Exception as e:
        error_mg=f'Error of API: {str(e)}'
        history.append({'role':'assistent', 'content':error_mg})
        return error_mg, history


