from app.tools.tool_executor import execute_tool

call = {
    "id": "call_003",
    "function": {
        "name": "unknown_tool",
        "arguments": {}
    }
}

print(execute_tool(call))
