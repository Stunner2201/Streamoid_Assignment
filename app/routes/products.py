# app/routes/products.py
from fastapi import APIRouter, Query, Depends
from sqlmodel import Session, select
from app.models import Product
from app.database import get_session
from typing import Optional

router = APIRouter(prefix="/products", tags=["Products"])

# List all products with pagination
@router.get("/")
def list_products(page: int = 1, limit: int = 10, session: Session = Depends(get_session)):
    offset = (page - 1) * limit
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    return products

# Search products with filters
@router.get("/search")
def search_products(
    brand: Optional[str] = Query(None),
    color: Optional[str] = Query(None),
    # minPrice: Optional[float] = Query(None),
    maxPrice: Optional[float] = Query(None),
    page: int = 1,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    query = select(Product)

    if brand:
        query = query.where(Product.brand == brand)
    if color:
        query = query.where(Product.color == color)
    if minPrice:
        query = query.where(Product.price >= minPrice)
    if maxPrice:
        query = query.where(Product.price <= maxPrice)

    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)

    products = session.exec(query).all()
    return products
