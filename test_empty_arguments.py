from app.tools.tool_executor import execute_tool

call = {
    "id": "call_007",
    "function": {
        "name": "get_order_status",
        "arguments": {"order_id": ""}
    }
}

print(execute_tool(call))
