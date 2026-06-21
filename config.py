
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

SENTIMENT_API = "https://huggingface.co/tabularisai/multilingual-sentiment-analysis"
model_name = "tabularisai/multilingual-sentiment-analysis"

model_gt='gpt2'

SUMMARIZE_API=''
model_sum='IlyaGusev/rut5_base_sum_gazeta'
# model_sum='t5-small'
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
