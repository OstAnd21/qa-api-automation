from pydantic import BaseModel


class Geo(BaseModel):
    lat: str
    lng: str

class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str
    
class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
    
class UserCreateRequest(BaseModel):
    name: str
    username: str
    email: str
    
class UserPatchRequest(BaseModel):
    name: str | None = None
    username: str | None = None
    email: str | None = None

class UserUpdateRequest(BaseModel):
    name: str
    username: str
    email: str
