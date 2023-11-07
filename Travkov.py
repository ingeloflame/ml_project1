! pip install class transformers
from transformers import pipeline
generator = pipeline(model="HuggingFaceH4/zephyr-7b-alpha")
generator("my favorite car")