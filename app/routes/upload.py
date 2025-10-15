# app/routes/upload.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Product
from app.utils.validators import validate_row
import pandas as pd
import os, uuid

router = APIRouter(prefix="/upload", tags=["Upload"])

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_csv(file: UploadFile = File(...), session: Session = Depends(get_session)):
    # ✅ Delete all old products first
    session.query(Product).delete()
    session.commit()

    # Save uploaded file
    contents = await file.read()
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)
    
    with open(path, "wb") as f:
        f.write(contents)

    # Read CSV
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {e}")

    # Ensure numeric fields
    df["mrp"] = pd.to_numeric(df["mrp"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df.get("quantity", 0), errors="coerce").fillna(0).astype(int)

    stored = 0
    failed = []

    for idx, row in df.iterrows():
        valid, error = validate_row(row)
        if not valid:
            failed.append({"row": idx + 1, "error": error})
            continue

        product = Product(
            sku=row["sku"],
            name=row["name"],
            brand=row["brand"],
            color=row.get("color"),
            size=row.get("size"),
            mrp=row["mrp"],
            price=row["price"],
            quantity=row["quantity"],
        )
        session.add(product)
        stored += 1

    session.commit()

    return {
        "stored": stored,
        "failed": failed,
        "saved_file": filename
    }