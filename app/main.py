from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.utils import generate_password, PasswordRequest

app = FastAPI()


# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-password")
async def password_api(data: PasswordRequest):
    password = generate_password(data)
    return JSONResponse(content={"password": password})
