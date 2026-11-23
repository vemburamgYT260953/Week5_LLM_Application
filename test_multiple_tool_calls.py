from app.tools.tool_executor import execute_tool

calls = [
    {
        "id": "call_009",
        "function": {
            "name": "get_order_status",
            "arguments": {"order_id": "1001"}
        }
    },
    {
        "id": "call_010",
        "function": {
            "name": "get_order_status",
            "arguments": {"order_id": "9999"}
        }
    }
]

for call in calls:
    print(execute_tool(call))
