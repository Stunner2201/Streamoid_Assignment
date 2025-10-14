# app/utils/validators.py
import pandas as pd

REQUIRED_FIELDS = ["sku", "name", "brand", "mrp", "price"]

def validate_row(row):
    # Check required fields
    for field in REQUIRED_FIELDS:
        if pd.isna(row.get(field)):
            return False, f"{field} is required"

    # Convert numeric fields
    try:
        mrp = float(row["mrp"])
        price = float(row["price"])
        quantity = int(row.get("quantity", 0))
    except ValueError:
        return False, "mrp, price, or quantity invalid"

    # Validation rules
    if price > mrp:
        return False, "price cannot be greater than mrp"
    if quantity < 0:
        return False, "quantity cannot be negative"

    return True, None
