from sqlalchemy.orm import Session
import models

def store_jokes(db: Session, jokes: list[dict]):
    """Store multiple jokes in the database"""
    for joke_data in jokes:
        joke = models.Joke(**joke_data)
        db.add(joke)
    db.commit()

def get_jokes(db: Session):
    """Retrieve all jokes from the database"""
    return db.query(models.Joke).all()
