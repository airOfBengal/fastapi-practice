from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from db.db_article import create_article, get_articles, get_article
from db.models import DbArticle

router = APIRouter(
    prefix="/article",
    tags=["article"]
)


@router.post("/", response_model=ArticleDisplay)
def create(request: ArticleBase, db: Session = Depends(get_db)):
    """
    Create a new article.
    """
    return create_article(db, request)

@router.get("/", response_model=list[ArticleDisplay])
def get_all(db: Session = Depends(get_db)):
    """
    Retrieve all articles.
    """
    return get_articles(db)

@router.get("/{id}", response_model=ArticleDisplay)
def get(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific article by its ID.
    """
    article = get_article(db, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

