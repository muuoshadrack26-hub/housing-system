from fastapi import FastAPI
from mdels import Base,Tenant
from database import db_dep, engine
from schema import CreateTenant
app=FastAPI()

Base.metadata.create_all(bind=engine)



@app.post("/tenant")
def create_tenant(session:db_dep,tenant_info:CreateTenant):
    user=Tenant(name=tenant_info.name,email=tenant_info.email,address=tenant_info.address,age=tenant_info.age,house_no=tenant_info.house_no,role=tenant_info.role)

    session.add(user)
    session.commit()
    session.refresh(user)

    return {"user_info":user}