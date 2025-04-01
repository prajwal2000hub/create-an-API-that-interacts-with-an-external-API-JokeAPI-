from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    type = Column(String, index=True)
    content = Column(String)
    nsfw = Column(Boolean)
    political = Column(Boolean)
    sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String)
