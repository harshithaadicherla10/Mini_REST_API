# Flask Mini REST API

A simple REST API built using Flask to manage books in memory.

## Features
- CRUD operations (Create, Read, Update, Delete)
- JSON request and response handling
- In-memory data storage
- RESTful API design

## Tech Stack
- Python
- Flask

## API Endpoints

| Method | Endpoint        | Description         |
|-------|----------------|---------------------|
| GET   | /books          | Get all books       |
| GET   | /books/<id>     | Get book by ID      |
| POST  | /books          | Add new book        |
| PUT   | /books/<id>     | Update book by ID   |
| DELETE| /books/<id>     | Delete book by ID   |

## Run Locally
```bash
pip install flask
python app.py
