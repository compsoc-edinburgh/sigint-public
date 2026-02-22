import fastapi
from fastapi import FastAPI, Cookie, Response, Request
from fastapi.responses import HTMLResponse

from base64 import b64encode, b64decode
from uuid import uuid4
import json 

with open("index.html", "r") as f: INDEX_HTML = f.read()
with open("admin.html", "r") as f: ADMIN_HTML = f.read()
with open("notAuth.html", "r") as f: NOT_AUTH_HTML = f.read()
with open("style-1.css", "r") as f: CSS = f.read()
with open("background.jpg", "rb") as f: BACKGROUND = f.read()

def encode(data:dict) -> str: return b64encode(json.dumps(data).encode()).decode()
def decode(data:str) -> dict: return json.loads(b64decode(data.encode()).decode())

def check_cookie(request: Request, response: Response) -> tuple[bool, Response]:
    try:
        decoded = decode(request.cookies.get("cookie", ""))

        # Check for broken cookies
        if not all(key in decoded for key in ["user_id", "user_auth"]):
            response.set_cookie(key="cookie", value=encode({"user_id": str(uuid4()), "user_auth": False}))
            return False, response
        
        # Check if the user is authenticated
        if decoded.get("user_auth") == True:
            return True, response
        
    except: # Handle any decoding errors
        response.set_cookie(key="cookie", value=encode({"user_id": str(uuid4()), "user_auth": False}))

    return False, response

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    response = HTMLResponse(content=INDEX_HTML)
    _, response = check_cookie(request, response)

    return response

@app.get("/admin", response_class=HTMLResponse)
async def read_admin(request: Request):
    auth, _ = check_cookie(request, HTMLResponse())

    response = HTMLResponse(content=(NOT_AUTH_HTML if not auth else ADMIN_HTML))
    _, response = check_cookie(request, response)
    return response


@app.get("/style.css", response_class=HTMLResponse)
async def read_style(request: Request): return check_cookie(request, HTMLResponse(content=CSS, media_type="text/css"))[1]

@app.get("/background.jpg", response_class=HTMLResponse)
async def read_background(request: Request): return check_cookie(request, HTMLResponse(content=BACKGROUND, media_type="image/jpeg"))[1]
