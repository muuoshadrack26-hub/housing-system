from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

Base=declarative_base()


class Tenant(Base):

    __tablename__="tenants"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False)
    name:Mapped[str]=mapped_column(String,nullable=False,index=True)
    email:Mapped[str]=mapped_column(String,nullable=False,index=True)
    address:Mapped[str]=mapped_column(String,nullable=False,index=True)
    house_no:Mapped[str]=mapped_column(String,nullable=False,index=True)
    age:Mapped[str]=mapped_column(String,nullable=False,index=True)
    role:Mapped[str]=mapped_column(String,nullable=False,index=True)



