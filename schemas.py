from pydantic import BaseModel

class Joke(BaseModel):
    id: int
    category: str
    type: str
    content: str
    nsfw: bool
    political: bool
    sexist: bool
    safe: bool
    lang: str

    class Config:
        orm_mode = True
