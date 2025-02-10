from typing import OrderedDict

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
        title="The Return of the King",
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}


@router.get("/", 
    response_model=OrderedDict[int, Book], 
    status_code=status.HTTP_200_OK,
    summary="Get all books",
    description="Retrieves a list of all books in the database",
    responses={
        200: {
            "description": "List of all books",
            "content": {
                "application/json": {
                    "example": {
                         1: Book(
                                id=1,
                                title="The Hobbit",
                                author="J.R.R. Tolkien",
                                publication_year=1937,
                                genre=Genre.SCI_FI,
                            ),
                            2: Book(
                                id=2,
                                title="The Lord of the Rings",
                                author="J.R.R. Tolkien",
                                publication_year=1954,
                                genre=Genre.FANTASY,
                            ),
                            3: Book(
                                id=3,
                                title="The Return of the King",
                                author="J.R.R. Tolkien",
                                publication_year=1955,
                                genre=Genre.FANTASY,
                            ),
                    }
                }
            }
        }
    }
)
async def get_books() -> OrderedDict[int, Book]:
    return db.get_books()


@router.post("/", 
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    description="Creates a new book in the database with the given details",
    responses={
        201: {
            "description": "Book created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 4,
                        "title": "New Book",
                        "author": "Author Name",
                        "publication_year": 2024,
                        "genre": "FICTION"
                    }
                }
            }
        },
        400: {
            "description": "Invalid book data",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid book data"}
                }
            }
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "publication_year"],
                                "msg": "value is not a valid integer",
                                "type": "type_error.integer"
                            }
                        ]
                    }
                }
            }
        }
    }
)
async def create_book(book: Book):
    try:
        db.add_book(book)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=book.model_dump()
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/{book_id}", 
    response_model=Book, 
    status_code=status.HTTP_200_OK,
    summary="Get a specific book",
    description="Retrieves a book by its ID",
    responses={
        200: {
            "description": "Book found",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "The Hobbit",
                        "author": "J.R.R. Tolkien",
                        "publication_year": 1937,
                        "genre": "FANTASY"
                    }
                }
            }
        },
        404: {
            "description": "Book not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Book not found"}
                }
            }
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["path", "book_id"],
                                "msg": "value is not a valid integer",
                                "type": "type_error.integer"
                            }
                        ]
                    }
                }
            }
        }
    }
)
async def get_book(book_id: int) -> Book:
    try:
        book = db.get_book(book_id)
        if book is None:
            raise KeyError("Book not found")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=book.model_dump()
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )


@router.put("/{book_id}", 
    response_model=Book, 
    status_code=status.HTTP_200_OK,
    summary="Update a book",
    description="Updates an existing book's details by its ID",
    responses={
        200: {
            "description": "Book updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "Updated Title",
                        "author": "Updated Author",
                        "publication_year": 2024,
                        "genre": "FICTION"
                    }
                }
            }
        },
        404: {
            "description": "Book not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Book not found"}
                }
            }
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "publication_year"],
                                "msg": "value is not a valid integer",
                                "type": "type_error.integer"
                            }
                        ]
                    }
                }
            }
        }
    }
)
async def update_book(book_id: int, book: Book) -> Book:
    try:
        updated_book = db.update_book(book_id, book)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=updated_book.model_dump()
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )


@router.delete("/{book_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a book",
    description="Deletes a book from the database by its ID",
    responses={
        204: {
            "description": "Book deleted successfully"
        },
        404: {
            "description": "Book not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Book not found"}
                }
            }
        }
    }
)
async def delete_book(book_id: int) -> None:
    try:
        db.delete_book(book_id)
        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT, 
            content=None
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
