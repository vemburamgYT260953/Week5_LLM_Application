
# Sample customer database
CUSTOMERS = {
    "C101": {
        "customer_id": "C101",
        "name": "Arun Kumar",
        "email": "arun@example.com",
        "membership": "Gold"
    },
    "C102": {
        "customer_id": "C102",
        "name": "Priya",
        "email": "priya@example.com",
        "membership": "Silver"
    },
    "C103": {
        "customer_id": "C103",
        "name": "Karthik",
        "email": "karthik@example.com",
        "membership": "Platinum"
    }
}


def get_customer(customer_id: str) -> dict:
    """Retrieve customer details using a customer ID."""

    customer = CUSTOMERS.get(customer_id)

    if customer is None:
        return {
            "error": f"Customer {customer_id} not found"
        }

    return customer
