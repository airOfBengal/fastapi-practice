from fastapi import FastAPI
from routers import blog_post, user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_post.router)
app.include_router(user.router)

@app.get('/')
def index():
    return {'message': 'Hello World!'}

models.Base.metadata.create_all(engine)
