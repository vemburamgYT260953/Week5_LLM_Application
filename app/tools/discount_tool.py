
def calculate_discount(
    amount: float,
    discount_percent: float
) -> dict:
    """Calculate discount amount and final price."""

    if amount <= 0:
        return {
            "error": "Amount must be greater than zero"
        }

    if not 0 <= discount_percent <= 100:
        return {
            "error": "Discount must be between 0 and 100"
        }

    discount_amount = amount * discount_percent / 100
    final_price = amount - discount_amount

    return {
        "original_amount": round(amount, 2),
        "discount_percent": discount_percent,
        "discount_amount": round(discount_amount, 2),
        "final_price": round(final_price, 2)
    }
