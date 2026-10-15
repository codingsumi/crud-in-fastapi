# FastAPI CRUD App

A small FastAPI project for learning how to build CRUD APIs.

## Why is there a `src` folder?

The `src` folder contains the Python package used by the application. Keeping
application code separate from project files helps prevent accidental imports
from the repository root and provides a clean structure as the project grows.

The `src` folder is not specifically for HTML files. If the application needs
HTML pages, place them in a `templates` directory inside the package. CSS,
JavaScript, and images normally belong in a `static` directory.

```text
src/
└── crud_app/
    ├── main.py
    ├── templates/
    │   └── index.html
    └── static/
        ├── css/
        ├── js/
        └── images/
```

For an API that only returns JSON, `templates` and `static` are not required.

## Run the current application

Install the dependencies and start the development server with `uv`:

```bash
uv sync
uv run fastapi dev main.py
```

Then open:

- API: <http://127.0.0.1:8000/posts>
- Interactive documentation: <http://127.0.0.1:8000/docs>
