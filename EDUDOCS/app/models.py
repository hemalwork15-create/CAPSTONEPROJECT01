from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    role = Column(Enum('admin', 'faculty', 'student'))
    password = Column(String(100))

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    file_path = Column(String(255))
    uploader_id = Column(Integer, ForeignKey('users.id'))
    upload_date = Column(TIMESTAMP)

    category = relationship("Category")
    uploader = relationship("User")
