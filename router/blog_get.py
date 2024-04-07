from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(prefix="/blog", tags=["blog"])

# @router.get('/all')
# def get_all():
#     return {'message': 'All blogs'}


@router.get("/all")
def get_all(page=1, page_size: Optional[int] = None):
    return {"message": f"All blogs on {page} with {page_size}"}


# ENUM TYPE
class BlogType(str, Enum):  # short is the enum and its value is 'short'
    short = "short"
    long = "long"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Displaying all blogs of type {type.value}"}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {"message": f"{id}, {comment_id}, {valid}, {username}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog_id(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        return {"message": f"Blog with id {id} found"}
