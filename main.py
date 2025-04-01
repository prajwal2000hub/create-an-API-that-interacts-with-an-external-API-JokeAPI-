from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud, schemas, httpx

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?amount=100"

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Joke API"}

@app.post("/fetch-jokes/")
async def fetch_and_store_jokes(db: Session = Depends(get_db)):
    """Fetch 100 jokes from JokeAPI and store in the database"""
    async with httpx.AsyncClient() as client:
        response = await client.get(JOKE_API_URL)
        data = response.json()

    jokes = []
    for joke in data["jokes"]:
        jokes.append({
            "category": joke["category"],
            "type": joke["type"],
            "content": joke.get("joke") if joke["type"] == "single" else f"{joke['setup']} - {joke['delivery']}",
            "nsfw": joke["flags"]["nsfw"],
            "political": joke["flags"]["political"],
            "sexist": joke["flags"]["sexist"],
            "safe": joke["safe"],
            "lang": joke["lang"]
        })

    # Store jokes in the database
    crud.store_jokes(db, jokes)
    return {"message": f"{len(jokes)} jokes stored successfully"}

@app.get("/jokes/", response_model=list[schemas.Joke])
def get_jokes(db: Session = Depends(get_db)):
    """Retrieve all stored jokes"""
    jokes = crud.get_jokes(db)
    return jokes
