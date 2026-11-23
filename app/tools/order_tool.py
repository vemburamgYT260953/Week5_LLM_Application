
# Sample order database
ORDERS = {
    "1001": {
        "order_id": "1001",
        "status": "Shipped",
        "delivery_date": "2026-11-25"
    },
    "1002": {
        "order_id": "1002",
        "status": "Processing",
        "delivery_date": "2026-11-28"
    },
    "1003": {
        "order_id": "1003",
        "status": "Delivered",
        "delivery_date": "2026-11-20"
    }
}


def get_order_status(order_id: str) -> dict:
    """Retrieve the status and delivery date of a customer order."""

    order = ORDERS.get(order_id)

    if order is None:
        return {
            "error": f"Order {order_id} not found"
        }

    return order
