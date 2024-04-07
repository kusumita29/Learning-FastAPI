from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    author: str
    published: bool


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: Optional[int] = 1):
    return {"id": id, "blog": blog, "version": version}
