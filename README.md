# create-an-API-that-interacts-with-an-external-API-JokeAPI-
This project implements a simple backend to create an API that interacts with an external API (JokeAPI), processes the data, and stores it in a database.

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
3. Stores the processed data in a database table.

## Project Requirements:
fastapi
uvicorn
httpx
sqlalchemy
python-dotenv

## How to setup and Run the Project:
Clone the repository.
Create Virtual Environment: python -m venv myenv
Install httpx: pip install httpx.
Install python-dotenv: pip install python-dotenv.
Install sqlalchemy: pip install sqlalchemy .
Install fastapi: pip install "fastapi[standard]".
Install uvicorn: pip install 'uvicorn[standard]'.
Run the Application: uvicorn main:app --reload.
Access the API: The API will be running on http://localhost:8000. Access the interactive API documentation at http://localhost:8000/docs.

