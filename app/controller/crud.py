from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.models import models 
from app.models import schemas 
from app.models.response import ResponseModel 

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

secretKey = "7c3fc4a49a24f44f57b24245767f7e1703f5100c7a46a48df5b67fe2df2b1870"
algorithm = "HS256"

def verifyPassword(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)

def getPasswordHash(password):
    return pwdContext.hash(password)

def authenticateUser(db: Session, email: str, password: str):
    user = getUserByEmail(db, email=email)
    if not user:
        return None
    if not verifyPassword(password, user.hashedPassword):
        return None
    return user

def createAccessToken(data: dict, expiresDelta: timedelta | None = None):
    toEncode = data.copy()
    if expiresDelta:
        expire = datetime.utcnow() + expiresDelta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    toEncode.update({"exp": expire})
    encodedJwt = jwt.encode(toEncode, secretKey, algorithm=algorithm)
    return encodedJwt

def createUser(db: Session, user: schemas.UserCreate)-> ResponseModel:
    passwordHashed = getPasswordHash(user.password)
    dbUser = models.User(username=user.username, hashedPassword=passwordHashed, email=user.email, birthday=user.birthday,
                          countryId=user.countryId, cityId=user.cityId, latitude=user.latitude, longitude=user.longitude)
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return ResponseModel(message="Usuario creado exitosamente")

def getUser(db: Session, userId: int):
    return db.query(models.User).filter(models.User.id == userId).first()

def getUserByEmail(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def getUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def putUser(db: Session, user: schemas.UserUpdate)-> ResponseModel:
    dbUser = getUser(db, user.id)
    passwordHashed = getPasswordHash(user.password)
    dbUser.username = user.username
    dbUser.hashedPassword = passwordHashed
    dbUser.email = user.email
    dbUser.birthday = user.birthday
    dbUser.countryId = user.countryId
    dbUser.cityId = user.cityId
    dbUser.latitude = user.latitude
    dbUser.longitude = user.longitude
    db.commit()
    return ResponseModel(message="Usuario actualizado exitosamente")

def removeUser(db: Session, id: int)-> ResponseModel:
    db.query(models.User).filter(models.User.id == id).delete()
    db.commit()
    return ResponseModel(message="Usuario eliminado exitosamente")


def createCountry(db: Session, country: schemas.CountryCreate)-> ResponseModel:
    dbCountry = models.Country(name=country.name)
    db.add(dbCountry)
    db.commit()
    db.refresh(dbCountry)
    return ResponseModel(message="País creado exitosamente")

def getCountry(db: Session, countryId: int):
    return db.query(models.Country).filter(models.Country.id == countryId).first()

def getCountryByName(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name == name).first()

def getCountries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def putCountry(db: Session, country: schemas.CountryUpdate)-> ResponseModel:
    dbCountry = getCountry(db, country.id)
    dbCountry.name = country.name
    db.commit()
    return ResponseModel(message="País actualizado exitosamente")

def removeCountry(db: Session, id: int)-> ResponseModel:
    db.query(models.Country).filter(models.Country.id == id).delete()
    db.commit()
    return ResponseModel(message="País eliminado exitosamente")


def createCity(db: Session, city: schemas.CityCreate)-> ResponseModel:
    dbCity = models.City(name=city.name)
    db.add(dbCity)
    db.commit()
    db.refresh(dbCity)
    return ResponseModel(message="Ciudad creada exitosamente")

def getCity(db: Session, cityId: int):
    return db.query(models.City).filter(models.City.id == cityId).first()

def getCityByName(db: Session, name: str):
    return db.query(models.City).filter(models.City.name == name).first()

def getCities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def putCity(db: Session, city: schemas.CityUpdate)-> ResponseModel:
    dbCity = getCity(db, city.id)
    dbCity.name = city.name
    db.commit()
    return ResponseModel(message="Ciudad actualizada exitosamente")

def removeCity(db: Session, id: int)-> ResponseModel:
    db.query(models.City).filter(models.City.id == id).delete()
    db.commit()
    return ResponseModel(message="Ciudad eliminada exitosamente")