from app.tools.tool_executor import execute_tool

call = {
    "id": "call_001",
    "function": {
        "name": "get_order_status",
        "arguments": {"order_id": "1001"}
    }
}

print(execute_tool(call))
