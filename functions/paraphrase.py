from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os

HF_TOKEN=os.getenv("HF_TOKEN")

_model = None
_tokenizer = None

def get_paraphraser():
    global _model, _tokenizer
    if _model is None:
        model_name = "cointegrated/rut5-base-paraphraser"
        try:
            # Загружаем с токеном, без force_download
            _tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
            _model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=HF_TOKEN)
        except Exception as e:
            # Если модель повреждена, пробуем принудительно перезагрузить
            print(f"Ошибка загрузки модели: {e}, пробуем перезагрузить с force_download=True")
            _tokenizer = AutoTokenizer.from_pretrained(model_name, force_download=True, token=HF_TOKEN)
            _model = AutoModelForSeq2SeqLM.from_pretrained(model_name, force_download=True, token=HF_TOKEN)
    return _model, _tokenizer

def paraphrase_text(text: str) -> str:
    """Перефразирует текст."""
    if not text.strip():
        return "Текст пуст."
    try:
        model, tokenizer = get_paraphraser()
        # Модель ожидает префикс "paraphrase: "
        input_text = "paraphrase: " + text
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=512,
                num_beams=4,
                early_stopping=True,
                no_repeat_ngram_size=3,
                temperature=0.9,
                do_sample=True
            )
        paraphrase = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return paraphrase
    except Exception as e:
        return f"Ошибка перефразирования: {str(e)}"