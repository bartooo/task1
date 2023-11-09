from project import db, app
from sqlalchemy.orm import validates


# Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"

    @validates("name")
    def validate_name(self, key, name):
        if not name.isalnum():
            raise ValueError("Name must contain only alphanumeric characters")
        if len(name) < 1 or len(name) > 64:
            raise ValueError("Name must be between 1 and 64 characters long")
        return name

    @validates("city")
    def validate_city(self, key, city):
        if not city.isalpha():
            raise ValueError("City must contain only letters")
        if len(city) < 1 or len(city) > 64:
            raise ValueError("City must be between 1 and 64 characters long")
        return city


with app.app_context():
    db.create_all()
