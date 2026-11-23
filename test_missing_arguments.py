from app.tools.tool_executor import execute_tool

call = {
    "id": "call_004",
    "function": {
        "name": "get_order_status",
        "arguments": {}
    }
}

print(execute_tool(call))
