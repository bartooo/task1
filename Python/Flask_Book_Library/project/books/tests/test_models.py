import pytest
from project.books.models import Book


def test_validate_name():
    with pytest.raises(ValueError):
        Book.validate_name(Book, "name", "Invalid Name!")

    with pytest.raises(ValueError):
        Book.validate_name(Book, "name", "a" * 65)

    assert Book.validate_name(Book, "name", "ValidName") == "ValidName"


def test_validate_author():
    with pytest.raises(ValueError):
        Book.validate_author(Book, "author", "Invalid Author!")

    with pytest.raises(ValueError):
        Book.validate_author(Book, "author", "a" * 65)

    assert Book.validate_name(Book, "name", "ValidAuthor") == "ValidAuthor"
