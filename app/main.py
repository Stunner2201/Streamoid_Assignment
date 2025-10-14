# app/main.py
from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.products import router as products_router
from app.database import create_db_and_tables

app = FastAPI(title="Streamoid Backend API")

# Create tables
create_db_and_tables()

# Include routers
app.include_router(upload_router)
app.include_router(products_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Streamoid Backend API is running!"}
