import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")


SENTIMENT_API = "https://huggingface.co/tabularisai/multilingual-sentiment-analysis"
# OBJECT_DETECTION_API = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
# TEXT_GEN_API = "https://api-inference.huggingface.co/models/gpt2"
# SUMMARIZATION_API = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# IMAGE_COLORIZATION_API = "https://api-inference.huggingface.co/models/johnj/colorization"
# EMOTION_API = "https://api-inference.huggingface.co/models/harsh3474/face-emotion-recognition"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}
