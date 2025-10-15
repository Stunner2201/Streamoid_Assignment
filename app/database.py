from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Store DB file inside /app/data (the mounted writable volume)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/test.db")

# ✅ Ensure /app/data exists
os.makedirs("data", exist_ok=True)

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
