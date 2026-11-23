
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Get the current status and expected delivery date of a customer order using its order ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The customer's order ID, for example 1001."
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_customer",
            "description": "Retrieve customer name, email and membership using a customer ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "The customer's unique ID, for example C101."
                    }
                },
                "required": ["customer_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_discount",
            "description": "Calculate the discount amount and final price for a purchase.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Original purchase amount. Must be greater than zero."
                    },
                    "discount_percent": {
                        "type": "number",
                        "description": "Discount percentage between 0 and 100."
                    }
                },
                "required": ["amount", "discount_percent"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]
