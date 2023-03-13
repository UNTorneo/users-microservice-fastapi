from datetime import date
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: str
    password: str

class UserBase(BaseModel):
    username : str
    birthday : date
    email: str
    country_id : int
    city_id : int
    latitude : float
    longitude : float 


class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    id: int 
    password: str

class User(UserBase):
    id: int 
    is_active: bool
    
    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    id: int 

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