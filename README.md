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
- Git & GitHub

## 📂 Project Structure

Mini_REST_API/

├── app.py

├── requirements.txt

└── README.md


## 🚀 Getting Started

### 1️⃣ Clone the Repository

''bash
git clone https://github.com/harshithaadicherla10/Mini_REST_API.git
cd Mini_REST_API

### 2️⃣ Install Dependencies
pip install flask

### 3️⃣ Run the Application
python app.py

Server will start at:

http://127.0.0.1:5000


## API Endpoints

| Method | Endpoint        | Description         |
|-------|----------------|---------------------|
| GET   | /books          | Get all books       |
| GET   | /books/<id>     | Get book by ID      |
| POST  | /books          | Add new book        |
| PUT   | /books/<id>     | Update book by ID   |
| DELETE| /books/<id>     | Delete book by ID   |

## 🧪 Sample JSON Data

Add Book (POST /books)
{
  "title": "Python Basics"
}

Response
{
  "id": 1,
  "title": "Python Basics"
}

## 🧠 Concepts Covered

- Flask routing
- HTTP methods (GET, POST, PUT, DELETE)
- REST API fundamentals
- JSON handling with jsonify()
- CRUD operations
- In-memory data management

## 🎯 Future Enhancements

- Database integration (MySQL / SQLite)
- Authentication & authorization
- Input validation
- API testing with unit tests
- Deployment to cloud platforms

## 👤 Author

Harshitha Adicherla
