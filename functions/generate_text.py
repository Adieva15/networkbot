from config import model_gt
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained(model_gt)
model = GPT2LMHeadModel.from_pretrained(model_gt)


# text = "Replace me by any text you'd like."
# encoded_input = tokenizer(text, return_tensors='tf')
# output = model(encoded_input)

def generate_text(prompt:str, max_length:int=100)->str:
    """
    Генерирует продолжение текста на основе заданного промпта.
    """
    try:
        inputs = tokenizer(prompt,
                           return_tensors="pt", # PyTorch тензоры
                           truncation=True,
                           padding=True,
                           max_length=512)
        with torch.no_grad():
            outputs=model.generate(
                input_ids=inputs.input_ids,
                attention_mask=inputs.attention_mask,
                max_length=max_length,
                num_return_sequences=1,
                pad_token_id=tokenizer.eos_token_id,
                do_sample=True,     # включаем вероятностную выборку
                temperature=0.7     # креативность (0 – детерминированно, 1 – случайно)
            )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return generated_text

    except Exception as e:
        return f'error of generaion: {str(e)}'