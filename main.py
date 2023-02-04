import os
import openai
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()


class ChatModel(BaseModel):
    model: Union[str, None] = 'text-davinci-003'
    prompt: str
    temperature: Union[float, None] = 0.7


def text_to_image(prompt: str):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    return image_url


@app.get('/')
async def root():
    return {'version': '1.0.0'}


@app.post('/')
async def chat(model: ChatModel):
    print(model)
    response = openai.Completion.create(
        model=model.model,
        prompt=model.prompt,
        temperature=model.temperature
    )
    result: str = response.choices[0].text
    result = result.removeprefix('\n\n')
    image = text_to_image(result)
    return {'result': result, 'image': image}


# Wrapper for lambda
handler = Mangum(app)
