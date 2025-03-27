from sqlalchemy import create_engine, Column , Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///./pet.db" #database location

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})#If False , the connection may be accessed in multiple threads; write operations may need to be serialized by the user to avoid data corruption.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()









# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# DATABASE_URL = "sqlite:///./test.db"  # Change this to your actual DB URL
#
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()























