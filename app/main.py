# app/main.py
from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.products import router as products_router
from app.database import create_db_and_tables, DATABASE_URL

import os
from app.database import create_db_and_tables
app = FastAPI(title="Streamoid Backend API")

# Create tables
create_db_and_tables()

# routers
app.include_router(upload_router)
app.include_router(products_router)

# Root endpoint
@app.get("/")

@app.on_event("startup")
def reset_db():
    if "sqlite" in DATABASE_URL:
        if os.path.exists("test.db"):
            os.remove("test.db")
        create_db_and_tables()
def root():
    return {"message": "Streamoid Backend API is running!"}
