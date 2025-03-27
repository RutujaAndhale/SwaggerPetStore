from database import Base, engine
from sqlalchemy import Column , Integer, String

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

class Store(Base):
    __tablename__="Store"
    id=Column(Integer,primary_key=True,index=True)
    petid=Column(Integer,index=True)
    name=Column(String,index=True)
    status=Column(String)

















#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from fastapi import FastAPI, Depends
# from typing import Dict, List
# from sqlalchemy.orm import Session
# from model import User, UserPayload, Base, engine, SessionLocal
# from pydantic import BaseModel
#
# Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# class UserCreate(BaseModel):
#     username: str
#     password: str
#
#
# @app.post("/users/")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     """
#     Create a new user with username and hashed password
#     """
#     # Create new user
#     db_user = User(username=user.username, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#
#     return {"message": "User created successfully"}
#
#
# @app.get("/name/", response_model=Dict[str, List[UserPayload]])
# def get_users(db: Session = Depends(get_db)) -> Dict[str, List[UserPayload]]:
#     """
#     Get all users
#     """
#     users = db.query(User).all()
#     return {"users": [UserPayload.from_orm(user) for user in users]}




# from fastapi import FastAPI#import
#
# app=FastAPI()#instance
#
# #get is an operation and in() path is included
# @app.get("/")#decorator
# def hello():#function/path operation function
#     return {'data':{'name':'rutu'}}
# #it means this operation(path operation function) we going to perform on this path(/'about') with this(get) operation
#
# @app.get('/about')
# def about():
#     return {"data":"about page"}
#
# #@app:-path opertaion decorator





# from fastapi import FastAPI
# from enum import Enum # used to give names to constants/ validating/fastapi give inbulit validation by using enum
#
# app=FastAPI()
#
# class AvailableFood(str,Enum):
#     indian='indian'
#     south='south'
#     italian='italian'
#
#
# food_items={"indian":['vadapav','pavbhaji'],
#             "south":['Dosa','idali'],
#             "italian":['pasta','pizza']}
# cupon_code={1:'10%',2:'20%',3:'30%'}
#
# @app.get('/get_items/{food}')
# def get_items(food:AvailableFood):
#     return food_items.get(food)
#
# @app.get('/get_cupon/{code}')
# def cupon(code:int):
#     return {"discount_amount":cupon_code.get(code)}