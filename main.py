from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "title": "Getting Started with Python",
        "content": "Python is a beginner-friendly programming language used for web development, automation, data analysis, and AI.",
        "author": "Michael Filip",
        "created_at": "2026-10-10T09:30:00",
    },
    {
        "id": 2,
        "title": "Building REST APIs with FastAPI",
        "content": "FastAPI makes it easy to build high-performance APIs with automatic validation, type hints, and interactive documentation.",
        "author": "Sarah Johnson",
        "created_at": "2026-10-11T14:15:00",
    },
    {
        "id": 3,
        "title": "Understanding Python Lists and Dictionaries",
        "content": "Lists store ordered collections of items, while dictionaries store data as key-value pairs. Both are essential Python data structures.",
        "author": "Rose Mary",
        "created_at": "2026-10-12T11:45:00",
    },
    {
        "id": 4,
        "title": "How Database Indexing Improves Performance",
        "content": "Database indexes help queries retrieve records faster by reducing the amount of data that needs to be scanned.",
        "author": "David Miller",
        "created_at": "2026-10-13T08:20:00",
    },
    {
        "id": 5,
        "title": "Introduction to Docker for Developers",
        "content": "Docker packages applications and their dependencies into containers, making development and deployment more consistent.",
        "author": "Rose Mary",
        "created_at": "2026-10-14T16:00:00",
    },
    {
        "id": 6,
        "title": "Async Programming in Python",
        "content": "Python's async and await syntax helps developers handle concurrent I/O operations efficiently, especially in API applications.",
        "author": "Michael Filip",
        "created_at": "2026-10-15T12:10:00",
    },
]


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(request, "about.html", {"title": "About"})


@app.get("/posts")
def get_posts():
    return {"status": 200, "data": posts}


# Authentication Routes
@app.get("/login")
def signin(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": "SignIn"})


@app.get("/register")
def signup(request: Request):
    return templates.TemplateResponse(request, "register.html", {"title": "Sign Up"})
