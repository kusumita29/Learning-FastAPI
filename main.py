from fastapi import FastAPI, Request, status, Response
from enum import Enum
from typing import Optional

from fastapi.responses import JSONResponse
from exceptions import StoryException
from router import user, article, product, blog_post, blog_get
from db import models
from db.database import engine


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


models.Base.metadata.create_all(engine)
