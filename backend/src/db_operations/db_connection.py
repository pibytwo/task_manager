"""DB connection"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_name = os.getenv("DB_NAME")
if not db_name:
    raise RuntimeError("Environment variable DB_NAME is not set. Shutting down app...")

# Ensure the data directory exists
os.makedirs("./data", exist_ok=True)

DATABASE_URL = f"sqlite:///./data/{db_name}.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
