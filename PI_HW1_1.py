from transformers import pipeline

translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")
translator("Мне нравится еда")