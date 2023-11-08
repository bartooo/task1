from project import db, app
import re
from sqlalchemy.orm import validates


# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer)
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    @validates('name')
    def validate_name(self, key, name):
        if not name.isalnum():
            raise ValueError('Name must contain only alphanumeric characters')
        if len(name) < 1 or len(name) > 64:
            raise ValueError('Name must be between 1 and 64 characters long')
        return name

    @validates('author')
    def validate_author(self, key, author):
        if not author.isalpha():
            raise ValueError('Author must contain only letters')
        if len(author) < 1 or len(author) > 64:
            raise ValueError('Author must be between 1 and 64 characters long')
        return author

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"


with app.app_context():
    db.create_all()
