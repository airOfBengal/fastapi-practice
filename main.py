from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routers import blog_post, user, article
from db import models
from db.database import engine
from exceptions import StoryException

app = FastAPI()
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(user.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Story error occurred: {exc.name}"}
    )   

models.Base.metadata.create_all(engine)
