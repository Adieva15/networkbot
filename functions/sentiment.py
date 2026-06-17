
from config import model_name
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def sentiment_analysis(text)->str:
    '''принимает строку, возвращает тональность'''
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        #вероятности классов
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred_class = torch.argmax(probabilities, dim=-1).item()

        if pred_class <= 1:
            return "Негативный"
        elif pred_class ==2:
            return "Нейтральный"
        else:
            return "Позитивный"

    except Exception as e:
        return f"Error: {str(e)}"
