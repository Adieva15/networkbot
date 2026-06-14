import requests
from config import SENTIMENT_API, headers

async def sentiment_analysis(text:str)->str:
    payload = {"inputs":text}
    try:
        response = requests.post(SENTIMENT_API, headers=headers, json=payload)
        result = response.json()
        if isinstance(result, list) and len(result)>0:
            labels = result[0]
            best = max(labels, key=lambda x: x['score'])
            label_map = {"LABEL_0":"негативный", "LABEL_1": "нейтральный", "LABEL_2": "позитивный"}
            return label_map.get(best['label'], best['label'])
        return "не удалось определить"
    except Exception as e:
        return f"Error: {str(e)}"