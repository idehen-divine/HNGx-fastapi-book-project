# FastAPI Book Management API

## Overview

Welcome to the **FastAPI Book Management API**, a lightweight yet powerful RESTful API designed to manage book collections efficiently. Built with **FastAPI**, this project ensures smooth **CRUD (Create, Read, Update, Delete) operations**, robust **input validation**, and clean **API documentation**.

## Features

- 🔥 **Fast and efficient** book management  
- ✅ **Input validation** powered by Pydantic  
- 📖 **Genre classification** using Enums  
- 🛡️ **Error handling** for a seamless experience  
- 🌍 **CORS support** for cross-origin access  
- 📝 **Auto-generated API documentation** via FastAPI  
- 🧪 **Unit-tested** endpoints for reliability  

## 🏗 Project Structure

```
fastapi-book-project/
├── api/
│   ├── db/
│   │   ├── __init__.py
│   │   └── schemas.py      # Data models and in-memory database
│   ├── routes/
│   │   ├── __init__.py
│   │   └── books.py        # Book route handlers
│   └── router.py           # API router configuration
├── core/
│   ├── __init__.py
│   └── config.py           # Application settings
├── tests/
│   ├── __init__.py
│   └── test_books.py       # API endpoint tests
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
└── README.md
```

## 🛠 Technologies Used

- 🐍 **Python 3.12**  
- ⚡ **FastAPI** - High-performance API framework  
- 📜 **Pydantic** - Data validation  
- 🔥 **Uvicorn** - ASGI server for production  
- 🧪 **pytest** - Testing framework  

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/idehen-divine/HNGx-fastapi-book-project.git
cd HNGx-fastapi-book-project
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### ▶ Running the Application

1. Start the server:

```bash
uvicorn main:app
```

2. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📡 API Endpoints 

### Books

| Method   | Endpoint                  | Description            |
| -------- | ------------------------- | ---------------------- |
| `GET`    | `/api/v1/books/`          | Get all books          |
| `GET`    | `/api/v1/books/{book_id}` | Retrieve a single book |
| `POST`   | `/api/v1/books/`          | Add a new book         |
| `PUT`    | `/api/v1/books/{book_id}` | Update a book          |
| `DELETE` | `/api/v1/books/{book_id}` | Remove a book          |

### Health Check

- `GET /healthcheck` - Check API status

## 📖 Book Schema  

```json
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "publication_year": 2024,
  "genre": "Fantasy"
}
```

Available genres:

- Science Fiction
- Fantasy
- Horror
- Mystery
- Romance
- Thriller

## ✅ Running Tests

```bash
pytest
```

## ❌ Error Handling

The API includes proper error handling for:

- Non-existent books
- Invalid book IDs
- Invalid genre types
- Malformed requests

## 🤝 Contributing 

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Need Help?  

If you have any questions or need support, feel free to **open an issue** in the repository. 
