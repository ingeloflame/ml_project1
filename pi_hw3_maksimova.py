#Группа 1, Максимова Н.В.
#Я пока не разобралась как реализовать весь функционал через fastAPI, так что переводчик переводит только то, что в переменной а
#Файл requirements.txt в репозитории присутствует, так что заново создавать его не было смысла
from transformers import pipeline

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def get_info():
    a = "Это было не так уж просто"
    translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")
    b = translator(a)
    return b


    