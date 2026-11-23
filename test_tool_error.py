from app.tools.tool_executor import execute_tool

call = {
    "id": "call_002",
    "function": {
        "name": "get_order_status",
        "arguments": {"order_id": "9999"}
    }
}

print(execute_tool(call))
