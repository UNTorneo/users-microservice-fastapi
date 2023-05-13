from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from app.controller.database import base

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashedPassword = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    birthday = Column(Date, nullable=False)
    countryId = Column(Integer, ForeignKey("countries.id"), nullable=False)
    cityId = Column(Integer, ForeignKey("cities.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    isActive = Column(Boolean, default=True)
    photoUrl = Column(String, nullable=True)
    country = relationship("Country", back_populates="citizens")
    city = relationship("City", back_populates="citizens")

class Country(base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    citizens = relationship("User", back_populates="country")

class City(base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    citizens = relationship("User", back_populates="city")