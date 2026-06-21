from config import SUMMARIZE_API, model_sum
from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch


tokenizer = AutoTokenizer.from_pretrained(model_sum)
model=T5ForConditionalGeneration.from_pretrained(model_sum)


def summarize_text(text:str)->str:
    try:
        tokenizer.pad_token=tokenizer.eos_token
        input_text = "summarize: " + text
        input_ids=tokenizer([input_text],
                         max_length=600,
                         add_special_tokens=True,
                         padding='max_length',
                         truncation=True,
                         return_tensors='pt')['input_ids']
        with torch.no_grad():
            output_ids=model.generate(
                input_ids=input_ids,
                max_length=200,
                min_length=30,
                no_repeat_ngram_size=4,
                num_beans=4,       # поиск по лучам для улучшения качества
                early_stopping=True
            )[0]

        summary = tokenizer.decode(output_ids, skip_special_tokens=True)
        return summary
    except Exception as e:
        return f"Error {str(e)}"