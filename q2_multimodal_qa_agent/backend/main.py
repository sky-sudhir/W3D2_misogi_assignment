from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import Optional
from PIL import Image
import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()
# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vision_model = genai.GenerativeModel("gemini-2.0-flash")
text_model = genai.GenerativeModel("gemini-2.0-flash")

def load_image_from_url(url: str):
    try:
        response = requests.get(url)
        return Image.open(BytesIO(response.content))
    except Exception as e:
        return None

@app.post("/ask")
async def ask_question(
    question: str = Form(...),
    image: Optional[UploadFile] = None,
    image_url: Optional[str] = Form(None)
):
    img = None
    if image:
        img = Image.open(BytesIO(await image.read()))
    elif image_url:
        img = load_image_from_url(image_url)

    try:
        if img:
            response = vision_model.generate_content([question, img])
        else:
            response = text_model.generate_content(question)

        return JSONResponse(content={
            "answer": response.text,
            "used_model": "gemini-2.0-flash" if img else "gemini-2.0-flash"
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "error": str(e)
        })
