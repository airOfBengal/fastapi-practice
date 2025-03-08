from typing import Optional
from fastapi import APIRouter, Response,status
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post('/new')
def create_blog(blog: BlogModel, response: Response):
    response.status_code = status.HTTP_200_OK
    return blog