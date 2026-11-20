from pydantic import BaseModel
from sqlalchemy.orm import Mapped


class CreateTenant(BaseModel):
    name: str
    email: str
    address: str
    house_no: str
    age: str
    role:str

class UpdateTenant(BaseModel):
    name: str
    email: str
    address:str
    house_no: str
    age: str
    role:str






