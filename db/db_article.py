from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleBase, ArticleDisplay


def create_article(db: Session, request: ArticleBase) -> DbArticle:
    """
    Create a new article in the database.
    """
    article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def get_articles(db: Session):
    """
    Retrieve all articles from the database.
    """
    return db.query(DbArticle).all()

def get_article(db: Session, id: int) -> DbArticle:
    """
    Retrieve a specific article by its ID.
    """
    return db.query(DbArticle).filter(DbArticle.id == id).first()

