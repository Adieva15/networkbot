
from config import model_name
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


# import os
# # Отключаем все прокси-переменные
# os.environ.pop('HTTP_PROXY', None)
# os.environ.pop('HTTPS_PROXY', None)
# os.environ.pop('http_proxy', None)
# os.environ.pop('https_proxy', None)
# os.environ.pop('ALL_PROXY', None)

# async def sentiment_analysis(text:str)->str:
#     payload = {"inputs":text}
#     try:
#         response = requests.post(SENTIMENT_API, headers=headers, json=payload)
#         result = response.json()
#         if isinstance(result, list) and len(result)>0:
#             labels = result[0]
#             best = max(labels, key=lambda x: x['score'])
#             label_map = {"LABEL_0":"негативный", "LABEL_1": "нейтральный", "LABEL_2": "позитивный"}
#             return label_map.get(best['label'], best['label'])
#         return "не удалось определить"
#     except Exception as e:
#         return f"Error: {str(e)}"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

async def sentiment_analysis(text)->str:
    '''принимает строку, возвращает тональность'''
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        #вероятности классов
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred_class = torch.argmax(probabilities, dim=-1).tolist()

        if pred_class <=1:
            return "Негативный"
        elif pred_class ==2:
            return "Нейтральный"
        else:
            return "Позитивный"

    except Exception as e:
        return f"Error: {str(e)}"
#
#
# texts = [
#     "I absolutely love the new design of this app!", "The customer service was disappointing.", "The weather is fine, nothing special.",
#     "Я в восторге от этого нового гаджета!", "Этот сервис оставил у меня только разочарование.", "Встреча была обычной, ничего особенного.",
#     ]
#
# for text, sentiment in zip(texts, sentiment_analysis(texts)):
#     print(f"Text: {text}\nSentiment: {sentiment}\n")
