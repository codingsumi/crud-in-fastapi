from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post.",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post.",
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post.",
    },
]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )


@app.get("/posts")
def get_posts():
    return {"status": 200, "data": posts}
