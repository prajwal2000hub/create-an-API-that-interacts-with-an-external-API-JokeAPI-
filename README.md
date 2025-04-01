# create-an-API-that-interacts-with-an-external-API-JokeAPI-
This project implements a simple backend to create an API that interacts with an external API: JokeAPI (https://sv443.net/jokeapi/v2/), processes the data, and stores it in a database.

## Task Details:
Build an API endpoint that performs the following operations:
1. Calls the JokeAPI to fetch a minimum of 100 jokes.
2. Extracts and processes the following columns from the fetched jokes:
a. category
b. type
c. joke (for "single" type) or setup and delivery (for "twopart" type)
d. flags.nsfw
e. flags.political
f. flags.sexist
g. safe
h. lang
4. Stores the processed data in a database table.

## Project Requirements:

1. fastapi.
2. uvicorn
3. httpx
4. sqlalchemy
5. python-dotenv

## How to setup and Run the Project:

1. Clone the repository.
2. Create Virtual Environment: python -m venv myenv.
3. Install httpx: pip install httpx.
4. Install python-dotenv: pip install python-dotenv.
5. Install sqlalchemy: pip install sqlalchemy.
6. Install fastapi: pip install "fastapi[standard]".
7. Install uvicorn: pip install 'uvicorn[standard]'.
8. Run the Application: uvicorn main:app --reload.
9. Access the API: The API will be running on http://localhost:8000. Access the interactive API documentation at http://localhost:8000/docs.


