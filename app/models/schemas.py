from datetime import date
from pydantic import BaseModel

class Token(BaseModel):
    accessToken: str

class Login(BaseModel):
    email: str
    password: str

class UserBase(BaseModel):
    username : str
    birthday : date
    email: str
    countryId : int
    cityId : int
    latitude : float
    longitude : float 
    photoUrl: str | None = None


class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None
    username: str | None = None
    birthday: date | None = None
    email: str | None = None
    countryId: int | None = None
    cityId: int | None = None
    latitude: float | None = None
    longitude: float | None = None

class User(UserBase):
    id: int 
    isActive: bool

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    id: int 

class City(CityBase):
    id: int

    class Config:
        orm_mode = True