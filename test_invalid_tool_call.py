from app.tools.tool_executor import execute_tool

call = {
    "id": "call_005",
    "function": {
        "arguments": {}
    }
}

print(execute_tool(call))
