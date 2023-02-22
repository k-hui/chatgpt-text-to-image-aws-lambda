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


class ImageModel(ChatModel):
    """
    allow ['256x256', '512x512', '1024x1024']
    """
    width: int = 1024
    height: int = 1024


def text_to_image(prompt: str, width: int, height: int):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=f'{width}x{height}'
    )
    image_url = response['data'][0]['url']
    print(image_url)
    return image_url


@app.get('/')
async def root():
    return {'version': '1.0.0'}


@app.post('/chat')
async def chat(model: ImageModel):
    response = openai.Completion.create(
        model=model.model,
        prompt=model.prompt,
        temperature=model.temperature,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    result: str = response.choices[0].text
    result = result.removeprefix('\n\n')
    result_image = text_to_image(result, model.width, model.height)
    return {'result': result, 'image': result_image}


@app.post('/image')
async def image(model: ImageModel):
    result_image = text_to_image(model.prompt, model.width, model.height)
    return {'image': result_image}


# Wrapper for lambda
handler = Mangum(app)
