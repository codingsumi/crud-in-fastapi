from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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


@app.get("/", response_class=HTMLResponse, include_in_schema=True)
@app.get("/html", response_class=HTMLResponse, include_in_schema=False)
def home():
    return "<h1>Welcome to the FastAPI Blog!</h1>"


@app.get("/posts")
def get_posts():
    return {"status": 200, "data": posts}
