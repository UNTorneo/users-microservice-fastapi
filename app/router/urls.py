from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import timedelta
from app.models import models 
from app.controller import crud
from app.controller.database import sessionLocal
from app.models import schemas
from fastapi import APIRouter
from app.models.failure import Failure
from app.models.schemas import Token
from app.models.response import ResponseModel

router = APIRouter()

accessTokenExpireMinutes = 30

# Dependency
def getDb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
async def loginForAccessToken(user: schemas.Login, db: Session = Depends(getDb))-> Token:
    dbUser = crud.authenticateUser(db, user.email, user.password)
    if not dbUser:
        raise Failure(detail="Email o contraseña incorrectos", status_code=404)
    accessTokenExpires = timedelta(minutes=accessTokenExpireMinutes)
    accessToken = crud.createAccessToken(
        data={"sub": dbUser.email}, expiresDelta=accessTokenExpires
    )
    return Token(accessToken=accessToken, tokenType="bearer")

@router.post("/users", response_model=ResponseModel)
def createUser(user: schemas.UserCreate, db: Session = Depends(getDb)):
    dbUser = crud.getUserByEmail(db, email=user.email)
    if dbUser:
        raise Failure(status_code=403, detail="Email ya registrado")
    return crud.createUser(db=db, user=user)

@router.get("/users", response_model=list[schemas.User])
def readUsers(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    users = crud.getUsers(db, skip=skip, limit=limit)
    return users

@router.get("/users/{userId}", response_model=schemas.User)
def readUser(userId: int, db: Session = Depends(getDb)):
    dbUser = crud.getUser(db, userId=userId)
    if dbUser is None:
        raise Failure(status_code=404, detail="Usuario no encontrado")
    return dbUser

@router.put("/users/{usersId}", response_model=ResponseModel)
def updateUser(user:schemas.UserUpdate, db: Session = Depends(getDb)):  
    dbUser = db.query(models.User).filter(models.User.id == user.id).first()
    if dbUser is None:
        raise Failure(status_code=404, detail="Usuario no encontrado")
    return crud.putUser(db=db, user=user)

@router.delete("/users/{userId}", response_model=ResponseModel)
def deleteUser(userId: int, db: Session = Depends(getDb)):
    dbUser = crud.getUser(db, userId=userId)
    if dbUser is None:
        raise Failure(status_code=404, detail="Usuario no encontrado")
    return crud.removeUser(db=db, id=userId)


@router.post("/countries", response_model=ResponseModel)
def createCountry(country: schemas.CountryCreate, db: Session = Depends(getDb)):
    dbCountry = crud.getCountryByName(db, name=country.name)
    if dbCountry:
        raise Failure(status_code=403, detail="País ya registrado")
    return crud.createCountry(db=db, country=country)

@router.get("/countries", response_model=list[schemas.Country])
def readCountries(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    countries = crud.getCountries(db, skip=skip, limit=limit)
    return countries

@router.get("/countries/{countryId}", response_model=schemas.Country)
def readCountry(countryId: int, db: Session = Depends(getDb)):
    dbCountry = crud.getCountry(db, countryId=countryId)
    if dbCountry is None:
        raise Failure(status_code=404, detail="País no encontrado")
    return dbCountry

@router.put("/countries/{countryId}", response_model=ResponseModel)
def updateCountry(country: schemas.CountryUpdate, db: Session = Depends(getDb)):
    dbCountry = db.query(models.Country).filter(models.Country.id == country.id).first()
    if dbCountry is None:
        raise Failure(status_code=404, detail="País no encontrado")
    return crud.putCountry(db=db, country=country)

@router.delete("/countries/{countryId}", response_model=ResponseModel)
def deleteCountry(countryId: int, db: Session = Depends(getDb)):
    dbCountry = crud.getCountry(db, countryId=countryId)
    if dbCountry is None:
        raise Failure(status_code=404, detail="País no encontrado")
    return crud.removeCountry(db=db, id=countryId)


@router.post("/cities", response_model=ResponseModel)
def createCity(city: schemas.CityCreate, db: Session = Depends(getDb)):
    dbCity = crud.getCityByName(db, name=city.name)
    if dbCity:
        raise Failure(status_code=403, detail="Ciudad ya registrada")
    return crud.createCity(db=db, city=city)

@router.get("/cities", response_model=list[schemas.City])
def readCities(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    cities = crud.getCities(db, skip=skip, limit=limit)
    return cities

@router.get("/cities/{cityId}", response_model=schemas.City)
def readCity(cityId: int, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=cityId)
    if dbCity is None:
        raise Failure(status_code=404, detail="Ciudad no encontrada")
    return dbCity

@router.put("/cities/{cityId}", response_model=ResponseModel)
def updateCity(city: schemas.CityUpdate, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=city.id)
    if dbCity is None:
        raise Failure(status_code=404, detail="Ciudad no encontrada")
    return crud.putCity(db=db, city=city)

@router.delete("/cities/{cityId}", response_model=ResponseModel)
def deleteCity(cityId: int, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=cityId)
    if dbCity is None:
        raise Failure(status_code=404, detail="Ciudad no encontrada")
    return crud.removeCity(db=db, id=cityId)