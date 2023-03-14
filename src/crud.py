from sqlalchemy.orm import Session

from . import models, schemas
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "7c3fc4a49a24f44f57b24245767f7e1703f5100c7a46a48df5b67fe2df2b1870"
ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_user(db: Session, user: schemas.UserCreate):
    password_hashed = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=password_hashed, email=user.email, birthday=user.birthday,
                          country_id=user.country_id, city_id=user.city_id, latitude=user.latitude, longitude=user.longitude)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def put_user(db: Session, user: schemas.UserUpdate):
    db_user = get_user(db, user.id)
    password_hashed = get_password_hash(user.password)
    db_user.username = user.username
    db_user.hashed_password = password_hashed
    db_user.email = user.email
    db_user.birthday = user.birthday
    db_user.country_id = user.country_id
    db_user.city_id = user.city_id
    db_user.latitude = user.latitude
    db_user.longitude = user.longitude
    db.commit()
    return {"message": "User updated successfully"}

def remove_user(db: Session, id: int):
    db.query(models.User).filter(models.User.id == id).delete()
    db.commit()
    return {"message": "User deleted successfully."}


def create_country(db: Session, country: schemas.CountryCreate):
    db_country = models.Country(name=country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_country_by_name(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name == name).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def put_country(db: Session, country: schemas.CountryUpdate):
    db_country = get_country(db, country.id)
    db_country.name = country.name
    db.commit()
    return {"message": "Country updated successfully"}

def remove_country(db: Session, id: int):
    db.query(models.Country).filter(models.Country.id == id).delete()
    db.commit()
    return {"message": "Country deleted successfully."}


def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()

def get_city_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.name == name).first()

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def put_city(db: Session, city: schemas.CityUpdate):
    db_city = get_city(db, city.id)
    db_city.name = city.name
    db.commit()
    return {"message": "City updated successfully"}

def remove_city(db: Session, id: int):
    db.query(models.City).filter(models.City.id == id).delete()
    db.commit()
    return {"message": "City deleted successfully"}