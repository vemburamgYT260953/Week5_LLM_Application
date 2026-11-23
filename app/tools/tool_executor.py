
import json

from app.tools.order_tool import get_order_status
from app.tools.customer_tool import get_customer
from app.tools.discount_tool import calculate_discount


TOOL_FUNCTIONS = {
    "get_order_status": get_order_status,
    "get_customer": get_customer,
    "calculate_discount": calculate_discount
}


def execute_tool(tool_call: dict) -> dict:
    """Execute one tool call and return its result with tool_call_id."""

    tool_call_id = tool_call.get("id", "unknown")

    try:
        function_data = tool_call["function"]
        tool_name = function_data["name"]
        arguments = function_data["arguments"]

        if tool_name not in TOOL_FUNCTIONS:
            result = {"error": f"Unknown tool: {tool_name}"}
        else:
            if isinstance(arguments, str):
                arguments = json.loads(arguments)

            if not isinstance(arguments, dict):
                raise ValueError("Tool arguments must be a JSON object")

            function = TOOL_FUNCTIONS[tool_name]
            result = function(**arguments)

    except (ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
        result = {"error": f"Invalid tool arguments: {error}"}

    except Exception as error:
        result = {"error": f"Tool execution failed: {error}"}

    return {
        "tool_call_id": tool_call_id,
        "role": "tool",
        "content": json.dumps(result)
    }
