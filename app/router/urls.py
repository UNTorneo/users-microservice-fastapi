from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.models import models 
from app.controller import crud
from app.controller.database import sessionLocal
from app.models import schemas
from fastapi import APIRouter

router = APIRouter()

accessTokenExpireMinutes = 30

# Dependency
def getDb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=schemas.Token)
async def loginForAccessToken(user: schemas.Login, db: Session = Depends(getDb)):
    dbUser = crud.authenticateUser(db, user.email, user.password)
    if not dbUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessTokenExpires = timedelta(minutes=accessTokenExpireMinutes)
    accessToken = crud.createAccessToken(
        data={"sub": dbUser.email}, expiresDelta=accessTokenExpires
    )
    return {"accessToken": accessToken, "tokenType": "bearer"}

@router.post("/users/", response_model=schemas.User)
def createUser(user: schemas.UserCreate, db: Session = Depends(getDb)):
    dbUser = crud.getUserByEmail(db, email=user.email)
    if dbUser:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.createUser(db=db, user=user)

@router.get("/users/", response_model=list[schemas.User])
def readUsers(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    users = crud.getUsers(db, skip=skip, limit=limit)
    return users

@router.get("/users/{userId}", response_model=schemas.User)
def readUser(userId: int, db: Session = Depends(getDb)):
    dbUser = crud.getUser(db, userId=userId)
    if dbUser is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dbUser

@router.put("/users/{usersId}")
def updateUser(user:schemas.UserUpdate, db: Session = Depends(getDb)):  
    dbUser = db.query(models.User).filter(models.User.id == user.id).first()
    if dbUser is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.putUser(db=db, user=user)

@router.delete("/users/{userId}")
def deleteUser(userId: int, db: Session = Depends(getDb)):
    dbUser = crud.getUser(db, userId=userId)
    if dbUser is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.removeUser(db=db, id=userId)


@router.post("/countries/", response_model=schemas.Country)
def createCountry(country: schemas.CountryCreate, db: Session = Depends(getDb)):
    dbCountry = crud.getCountryByName(db, name=country.name)
    if dbCountry:
        raise HTTPException(status_code=400, detail="Country already registered")
    return crud.createCountry(db=db, country=country)

@router.get("/countries/", response_model=list[schemas.Country])
def readCountries(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    countries = crud.getCountries(db, skip=skip, limit=limit)
    return countries

@router.get("/countries/{countryId}", response_model=schemas.Country)
def readCountry(countryId: int, db: Session = Depends(getDb)):
    dbCountry = crud.getCountry(db, countryId=countryId)
    if dbCountry is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return dbCountry

@router.put("/countries/{countryId}")
def updateCountry(country: schemas.CountryUpdate, db: Session = Depends(getDb)):
    dbCountry = db.query(models.Country).filter(models.Country.id == country.id).first()
    if dbCountry is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return crud.putCountry(db=db, country=country)

@router.delete("/countries/{countryId}")
def deleteCountry(countryId: int, db: Session = Depends(getDb)):
    dbCountry = crud.getCountry(db, countryId=countryId)
    if dbCountry is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return crud.removeCountry(db=db, id=countryId)


@router.post("/cities/", response_model=schemas.City)
def createCity(city: schemas.CityCreate, db: Session = Depends(getDb)):
    dbCity = crud.getCityByName(db, name=city.name)
    if dbCity:
        raise HTTPException(status_code=400, detail="City already registered")
    return crud.createCity(db=db, city=city)

@router.get("/cities/", response_model=list[schemas.City])
def readCities(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    cities = crud.getCities(db, skip=skip, limit=limit)
    return cities

@router.get("/cities/{cityId}", response_model=schemas.City)
def readCity(cityId: int, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=cityId)
    if dbCity is None:
        raise HTTPException(status_code=404, detail="City not found")
    return dbCity

@router.put("/cities/{cityId}")
def updateCity(city: schemas.CityUpdate, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=city.id)
    if dbCity is None:
        raise HTTPException(status_code=404, detail="City not found")
    return crud.putCity(db=db, city=city)

@router.delete("/cities/{cityId}")
def deleteCity(cityId: int, db: Session = Depends(getDb)):
    dbCity = crud.getCity(db, cityId=cityId)
    if dbCity is None:
        raise HTTPException(status_code=404, detail="City not found")
    return crud.removeCity(db=db, id=cityId)