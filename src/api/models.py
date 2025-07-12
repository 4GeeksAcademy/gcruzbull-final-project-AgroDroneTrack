from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable = False)
    phone_number: Mapped[int] = mapped_column(Integer, nullable = False, default = "")
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    farm_location: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    farm_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    avatar: Mapped[str] = mapped_column(String(120), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(200), nullable=False) 
    salt: Mapped[str] = mapped_column(String(80), nullable = False, default = 1 )

    farm: Mapped[list["Farm"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.first_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "farm_location": self.farm_location,
            "farm_name": self.farm_name,
            "avatar": self.avatar,
            "password": self.password,
            "accept_terms": self.accept_terms,
            "salt": self.salt,     
            # do not serialize the password, its a security breach
        }
    
class NDVI_images(db.Model):
    __tablename__ = "ndvi_images"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    farm_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    farm_location: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    ndvi_url: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    farm: Mapped[list["Farm"]] = relationship(back_populates="ndvi_images")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "farm_location": self.farm_location,
            "farm_name": self.farm_name,
            "ndvi_url": self.ndvi_url    
        }

class Aereal_images(db.Model):
    __tablename__ = "aereal_images"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    farm_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    farm_location: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    aereal_url: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    farm: Mapped[list["Farm"]] = relationship(back_populates="aereal_images")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "farm_location": self.farm_location,
            "farm_name": self.farm_name,
            "aereal_url": self.aereal_url,    
        }
    
class Farm(db.Model):
    __tablename__ = "farm"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    ndvi_images_id: Mapped[int] = mapped_column(ForeignKey("ndvi_images.id"), nullable=False)
    aereal_images: Mapped[int] = mapped_column(ForeignKey("aereal_images.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="farm")
    ndvi: Mapped["NDVI_images"] = relationship(back_populates="farm")
    aereal: Mapped["Aereal_images"] = relationship(back_populates="farm")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "ndvi_images_id": self.farm_location,
            "aereal_images_id": self.farm_name,
        }
