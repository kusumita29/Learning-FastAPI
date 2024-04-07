from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
from router import user, article
from router import blog_get
from router import blog_post
from db import models
from db.database import engine


app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World!"}


models.Base.metadata.create_all(engine)
