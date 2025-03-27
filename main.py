from fastapi import FastAPI
from database import Base, engine
from enum import Enum #used to give names to constants/ validating/fastapi give inbulit validation by using enum
from apps.pet import router as pet_router
from apps.store import router as store_router
from apps.user import router as user_router


app=FastAPI(title="Swagger Petstore",openapi_tags=[{"name":"Pets","description":"Everything about your Pets"},
                                                   {"name":"Store","description":"Access to Petstore orders"},
                                                   {"name":"Users","description":"Operations about user"}])

#if table is not exist in DB it will crate it.
Base.metadata.create_all(bind=engine)#engine is typically a global object created just once for a particular database server

app.include_router(pet_router)
app.include_router(store_router)
app.include_router(user_router)


# app.include_router(pet_router, prefix="/pet", tags=["Pets"])
# app.include_router(user_router, prefix="/user", tags=["Users"])

#@app.get("/")
def home():
    return {"message": "welcome to pet shop"}






















# from fastapi import FastAPI
# from enum import Enum #used to give names to constants/ validating/fastapi give inbulit validation by using enum
# from pet import router as pet_router
# from store import router as store_router
# from user import router as user_router
# from database import SessionLocal
# from database import Base,engine
# Base.metadata.create_all(bind=engine)#if table not exist in db it will create it
#
# app=FastAPI(title="Swagger Petstore",openapi_tags=[{"name":"Pets","description":"Everything about your Pets"},
#                                                    {"name":"Store","descripton":"Access to Petstore orders"},
#                                                    {"name":"Users","description":"Operations about user"}])
#
# app.include_router(pet_router)
# app.include_router(store_router)
# app.include_router(user_router)
#
# # @app.get('/')
# def home():
#   return {"msg":"welcome to pet shop"}