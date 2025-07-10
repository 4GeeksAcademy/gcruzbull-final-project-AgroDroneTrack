from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable = False)
    last_name: Mapped[str] = mapped_column(String(50), nullable = False)
    phone_number: Mapped[int] = mapped_column(Integer, nullable = False, default = "")
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False) 
    salt: Mapped[str] = mapped_column(String(80), nullable = False, default = 1 )

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "password": self.password,
            "accept_terms": self.accept_terms,
            "salt": self.salt,     
            # do not serialize the password, its a security breach
        }